#Amoout/accounts/forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from captcha.fields import CaptchaField

class CustomerUserCreationForm(UserCreationForm):
    captcha = CaptchaField()#adds the captcha
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CaptchatestForm(forms.Form):
    myfield= forms.CharField(label="My Feild", max_length=100)
    captcha = CaptchaField()