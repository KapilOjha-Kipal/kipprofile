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

def form(request):
    op=0
    try:
        a=int(request.GET['n1'])
        b= int(request.GET['n2'])
       
        op = a+b
    except:
        print('not calculate')
    return render(request,'form.html', {'output' : op} )

