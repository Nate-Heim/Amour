#Amour/accounts/urls.py
from accounts.views import profile_view
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import SignUpView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define the login view
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("captcha/", include("captcha.urls")),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit')
]

#Profile Pic related work (Under work by Colin DONT TOUCH!!)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
