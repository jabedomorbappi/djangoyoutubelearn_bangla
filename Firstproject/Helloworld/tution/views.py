from django.shortcuts import render
from .models import Contact
from .forms import ContactForm,ContactFormModel

# Create your views here.

def contact(request):
    if request.method=="POST":
        form=ContactFormModel(request.POST)
        if form.is_valid():
            
            form.save()

    else:
        form=ContactForm()
            
    return render(request,'contact.html',{"form":form}) 
