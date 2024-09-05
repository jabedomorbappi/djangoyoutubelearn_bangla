from django.shortcuts import render, redirect
from .models import ImageDescription
from .forms import ImageForm

def imageshow(request):
    image_d = ImageDescription.objects.all()
    return render(request, 'imgfiled/postview.html', {'image_d': image_d})

def loadimage(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imageshow')
    else:
        form = ImageForm()
    
    return render(request, 'imgfiled/load_image.html', {"form": form})
