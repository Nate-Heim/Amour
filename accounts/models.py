# Amour/accounts/models.py
from django.contrib.auth.models import AbstractUser
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