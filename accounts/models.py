# Amour/accounts/models.py
from django.contrib.auth.models import AbstractUser
from survey.models import UserResponse
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True, blank=True)

    # Add new fields
    interests = models.TextField(
        max_length=500, 
        blank=True, 
        null=True, 
        help_text="Write a brief description of your interests."
    )
    bio = models.TextField(
        max_length=300, 
        blank=True, 
        null=True, 
        help_text="Write a short bio about yourself."
    )

    DESIRE_CHOICES = [
        ("relationship", "Relationship"),
        ("friendship", "Friendship"),
        ("fling", "Fling"),
        ("other", "Other"),
        ("soulmate", "Soulmate"),
    ]
    Desires = models.CharField(
        max_length=50,
        choices=DESIRE_CHOICES,
        null=True,
        blank=True,
    )

    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        blank=True,
    )

    def calculate_match_percentage(self, other_user):
        user1_responses = UserResponse.objects.filter(user=self)
        user2_responses = UserResponse.objects.filter(user=other_user)

        if not user1_responses.exists() or not user2_responses.exists():
            return 0

        user1_dict = {response.question.id: response.response for response in user1_responses}
        user2_dict = {response.question.id: response.response for response in user2_responses}

        common_questions = set(user1_dict.keys()).intersection(set(user2_dict.keys()))
        if not common_questions:
            return 0

        matching_answers = sum(
            1 for qid in common_questions if user1_dict[qid] == user2_dict[qid]
        )
        return (matching_answers / len(common_questions)) * 100