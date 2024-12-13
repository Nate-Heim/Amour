from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":
        ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":
        ("age",)}),)
    
admin.site.register(CustomUser, CustomUserAdmin)
