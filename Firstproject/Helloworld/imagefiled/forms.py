from django import forms
from .models import ImageDescription

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageDescription
        fields = '__all__'
