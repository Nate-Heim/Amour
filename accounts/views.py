#Amour/accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib import messages

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
        user.desires = request.POST.get('desires')
        if request.FILES.get('profile_pic'):
            user.profile_pic = request.FILES['profile_pic']
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the profile view after saving

    desires_choices = CustomUser._meta.get_field('Desires').choices
    return render(request, 'profileEdit.html', {'user': request.user, 'desires_choices': desires_choices})