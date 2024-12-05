#Amour/accounts/models.py
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=10, null=True, blank=True)

    # Add a field to store the selected desire
    DESIRE_CHOICES = [
        ('relationship', 'Relationship'),
        ('friendship', 'Friendship'),
        ('fling', 'Fling'),
        ('other', 'Other'),
        ('soulmate', 'Soulmate'),
    ]

    Desires = models.CharField(
        max_length=50,
        choices=DESIRE_CHOICES,
        null=True,
        blank=True,
    )

    #Starting the work for adding profile pictures
    profile_pic = models.ImageField(
        upload_to='profile_pics/', #This is me making a directory for the profile pictures called "profile_pics/"
        null=True,
        blank=True,
    )
    