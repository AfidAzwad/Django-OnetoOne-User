from django import forms
from django.db.models import fields
from crud import models


class Userform(forms.ModelForm):
    class Meta:
        model = models.Userprofile
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
        }


class Users(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "password")
