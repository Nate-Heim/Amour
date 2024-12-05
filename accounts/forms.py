#Amoout/accounts/forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from captcha.fields import CaptchaField




class CustomerUserCreationForm(UserCreationForm):
    captcha = CaptchaField()#adds the captcha
    
    DESIRE_CHOICES = [
    ('relationship', 'Relationship'),
    ('friendship', 'Friendship'),
    ('fling', 'Fling'),
    ('other', 'Other'),
    ('soulmate', 'Soulmate'),
]
    Desires = forms.ChoiceField(
    choices=DESIRE_CHOICES,
    label="What are you looking for?",
    required=True,
    widget=forms.Select(attrs={"class": "form-control"}) #This was optional and it just adds some CSS classes
)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "Gender",
            "Desires",
            "profile_pic",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "Gender",
            "Desires",
            "profile_pic",
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_pic', 'Desires', 'age', 'Gender']
        widgets = {
            'desires': forms.Select(attrs={'class': 'form-control'}),
        }
class CaptchatestForm(forms.Form):
    myfield= forms.CharField(label="My Field", max_length=100)
    captcha = CaptchaField()