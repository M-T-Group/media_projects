from django import forms
from .models import Image
from django.contrib.auth.models import User


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
