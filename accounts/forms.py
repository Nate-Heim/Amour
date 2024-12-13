#Amour/accounts/forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from captcha.fields import CaptchaField

class CustomerUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
            "Gender",
            "Desires",
            "profile_pic",
            "interests",
            "bio",
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
        fields = ['profile_pic', 'Desires', 'age', 'Gender', 'interests', 'bio']
        widgets = {
            'Desires': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'interests': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
class CaptchatestForm(forms.Form):
    myfield= forms.CharField(label="My Field", max_length=100)
    captcha = CaptchaField()