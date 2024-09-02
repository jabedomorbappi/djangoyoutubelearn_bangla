from django.shortcuts import render,HttpResponse

def home(request):
    name=['jabed','omor','bappi']
    context={'name':name}
    return render(request,'home.html',context)


