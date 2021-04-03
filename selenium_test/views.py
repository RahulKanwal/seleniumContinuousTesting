from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
   if(request.method == 'POST'):
        name = request.POST['username']
        password = request.POST['pass']
        if(name=="human" and password == "root"):
            return render(request,'success.html')
   return render(request,'index.html')
    
