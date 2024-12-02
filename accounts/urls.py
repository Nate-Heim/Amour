#Amour/accounts/urls.py
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define the login view
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("captcha/", include("captcha.urls")),
]
