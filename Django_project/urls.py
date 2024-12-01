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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("publicPages.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("_debug_/", include(debug_toolbar.urls)),
    path("captcha/", include("captcha.urls")),
    re_path(r"", include("django_private_chat2.urls", namespace="django_private_chat2")),
]
