#Amour/accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

class SignUpView(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')  # Redirect after successful sign-up
    template_name = 'registration/signup.html'


#Special view for profile page
@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.age = request.POST.get('age')
        user.Gender = request.POST.get('Gender')
        user.desires = request.POST.get('desires')
        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES['profile_picture']
        user.save()
        return redirect('profile')
    
    desires_choices = CustomUser._meta.get_field('Desires').choices
    return render(request, 'profile.html', {'desires_choices': desires_choices})