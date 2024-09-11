from django.shortcuts import render

# Create your views here.

def one_home(request):
    return render(request,"onetoone/one_home.html")
