from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title':'Home Page New',
        'body1':'this is made by using directories',
        'klist': [ 'cat' , 'dog' ,'cow']
            
            }
    return render(request,"index.html",data)

def hello(request,hello):
    return HttpResponse(hello)