from django.shortcuts import render,redirect
from .forms import DataForm
from .models import Data

# Create your views here.
def firstApp(request):
    return render(request,'firstapp/home.html')

def data(request):
    if request.method=="POST":
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success') 
    else:
        form=DataForm()
    return render(request,'data.html',{'form':form})

def success_view(request):
    return render(request, 'success.html')
            
def postview(request):
    data= Data.objects.all()
    return render(request,'firstapp/data_view.html',{"data":data})
 
               