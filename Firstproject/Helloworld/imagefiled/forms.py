from django import forms
from .models import Imagedescription

class ImagedescriptionForm(forms.ModelForm):
    class Meta:
        model = Imagedescription
        fields = ['name', 'title', 'image', 'available', 'details', 'MEDIUM']
        
        widgets = {
            'available': forms.CheckboxInput(),
            'details': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
