from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('survey/', login_required(views.take_survey), name='take-survey'),
    path('survey/thank-you/', views.survey_thank_you, name='survey-thank-you'),
]