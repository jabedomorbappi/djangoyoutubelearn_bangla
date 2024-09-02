from django.shortcuts import render,HttpResponse

def home(request):
    if request.method=="GET":
        
        name=['jabed','omor','bappi']
        context={'name':name}
        return render(request,'home.html',context)


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        content=request.POST['contact']
        print(name)
        print(phone)
        print(content)
    return render(request,'contact.html')    
        
        
    