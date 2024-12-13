#survey/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User  # Optional: for linking responses to users
from django.core.exceptions import ValidationError
import json

class SurveyQuestion(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('boolean', 'Boolean'),
        ('choice', 'Choice'),
    ]
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='boolean')
    options = models.JSONField(blank=True, null=True)

    def clean(self):
        if self.options is not None:
            try:
                # Validate `options` as JSON
                json.dumps(self.options)
            except (TypeError, ValueError):
                raise ValidationError("Invalid JSON format for options field.")

class UserResponse(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)  # Use AUTH_USER_MODEL
    response = models.TextField()  # Store the user's response

    def __str__(self):
        return f"Response to {self.question} by {self.user}"