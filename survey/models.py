from django.db import models

class SurveyQuestion(models.Model):
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, default='boolean')
    options = models.TextField(null=True, blank=True)  # For multiple-choice questions

    def __str__(self):
        return self.question_text