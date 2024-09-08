from django.shortcuts import render,redirect
from .models import Imagedescription
from .forms import ImagedescriptionForm

# Create your views here.

def createimagedescription(request):
    if request.method=="POST":
        form=ImagedescriptionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('')
    else:
        form=  ImagedescriptionForm()
    return render(request, 'template_name.html', {'form': form}) 
      
def success_page(request):
    images = Imagedescription.objects.all()  # Load images for success page  
    return render(request, 'success.html', {'images': images})          
     
    
    
    