#Amour/accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib import messages

###
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class SignUpView(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')  # Redirect after successful sign-up
    template_name = 'registration/signup.html'
    
###
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')
#Special view for profile page
###


@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.age = request.POST.get('age')
        user.Gender = request.POST.get('Gender')
        user.Desires = request.POST.get('Desires')
        user.interests = request.POST.get('interests')
        user.bio = request.POST.get('bio')
        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES['profile_pic']
        user.save()
        return redirect('profile')

    desires_choices = CustomUser._meta.get_field('Desires').choices
    return render(request, 'profile.html', {'desires_choices': desires_choices})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.age = request.POST.get('age')
        user.Gender = request.POST.get('Gender')
        user.Desires = request.POST.get('Desires')
        user.interests = request.POST.get('interests')
        user.bio = request.POST.get('bio')
        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES['profile_pic']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    desires_choices = CustomUser._meta.get_field('Desires').choices
    return render(request, 'profileEdit.html', {'user': request.user, 'desires_choices': desires_choices})