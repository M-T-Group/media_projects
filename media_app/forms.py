from django import forms
from .models import Image


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner']
