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
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control is-peach"}),
            "email": forms.EmailInput(attrs={"class": "form-control is-peach"}),
            "age": forms.NumberInput(attrs={"class": "form-control is-peach"}),
            "Gender": forms.TextInput(attrs={"class": "form-control is-peach"}),
            "Desires": forms.Select(attrs={"class": "form-control is-peach"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control is-peach"}),
            "interests": forms.Textarea(
                attrs={"class": "form-control is-peach", "rows": 5}
            ),
            "bio": forms.Textarea(attrs={"class": "form-control is-peach", "rows": 3}),
        }

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
            'profile_pic': forms.FileInput(attrs={'class': 'form-control is-peach'}),
            'Desires': forms.Select(attrs={'class': 'form-control is-peach'}),
            'age': forms.NumberInput(attrs={'class': 'form-control is-peach'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control is-peach'}),
            'bio': forms.Textarea(attrs={'class': 'form-control is-peach', 'rows': 3}),
            'interests': forms.Textarea(attrs={'class': 'form-control is-peach', 'rows': 5}),
        }
class CaptchatestForm(forms.Form):
    myfield= forms.CharField(label="My Field", max_length=100)
    captcha = CaptchaField()