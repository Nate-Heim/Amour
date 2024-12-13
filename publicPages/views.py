#Amour/publicPages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from survey.models import UserResponse  # Import your model

from django.shortcuts import render
from django.views.generic import TemplateView
from survey.models import UserResponse  # Import your model

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            # Retrieve all responses for the logged-in user
            user_responses = UserResponse.objects.filter(user=self.request.user)
            
            responses = [
                (response.question.question_text, response.response) for response in user_responses
            ]
            context['responses'] = responses
        else:
            context['responses'] = None  # No responses for unauthenticated users

        return context