from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label='Your Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
    )
    phone = forms.CharField(
        max_length=100, 
        label='Your Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number',
        })
    )
    content = forms.CharField(
        max_length=100, 
        label='Your Content',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message',
            'rows': 4,
        })
    )
from .models import Contact    
class ContactFormModel(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

    
