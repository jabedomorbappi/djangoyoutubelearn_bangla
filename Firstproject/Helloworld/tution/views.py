from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            content=form.cleaned_data['content']
            obj=Contact(name=name,phone=phone,content=content)
            obj.save()
            print(name)
            print(phone)
            print(content)
            
    else:
        form=ContactForm()
            
    return render(request,'contact.html',{"form":form}) 
