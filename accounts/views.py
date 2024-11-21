#Amour/accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm

class SignUpView(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')  # Redirect after successful sign-up
    template_name = 'registration/signup.html'
