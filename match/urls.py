#match/urls.py
from django.urls import path
from .views import find_matches

urlpatterns = [
    path('find/', find_matches, name='find_matches'),
]