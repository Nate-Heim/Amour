"""
URL configuration for Django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Amour/Django_project/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from django.contrib.auth import views as auth_views
from accounts.views import profile_view
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import ResetPasswordView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("publicPages.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("_debug_/", include(debug_toolbar.urls)),
    path("captcha/", include("captcha.urls")),
    re_path(r"", include("django_private_chat2.urls", namespace="django_private_chat2")),
    path('profile/', profile_view, name='profile'),
    path('chat/', include('chat.urls')),
    path('survey/', include("survey.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('match/', include('match.urls')),
]
#Think this needs to be in Django urls as well to serve the photo

#Profile Pic related work (Under work by Colin DONT TOUCH!!)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
