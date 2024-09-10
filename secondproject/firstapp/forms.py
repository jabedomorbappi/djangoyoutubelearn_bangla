from django import forms
from .models import Data


# class DataForm(forms.ModelForm):
    
#     class Meta:
#         model=Data
#         fields="__all__"
        
# forms.py
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'age', 'category', 'medium', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded',
                'placeholder': 'Enter your name',
                'required': 'required',
                'maxlength': '100',  # Limit the length of the input
                'aria-label': 'Full Name'  # Accessibility label
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control rounded',
                'placeholder': 'Enter your age',
                'required': 'required',
                'min': '0',  # Minimum value
                'max': '120',  # Maximum value
                'step': '1',  # Step for number input
                'aria-label': 'Age'  # Accessibility label
            }),
            'category': forms.Select(attrs={
                'class': 'form-control rounded',
                'required': 'required',
                'aria-label': 'Select Category'  # Accessibility label
            }),
            'medium': forms.SelectMultiple(attrs={
                'class': 'form-control rounded',
                'required': 'required',
                'size': '5',  # Show multiple options
                'aria-label': 'Select Medium'  # Accessibility label
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control rounded',
                'accept': 'image/*',  # Accept only image files
                'aria-label': 'Upload Profile Image'  # Accessibility label
            }),
        }
