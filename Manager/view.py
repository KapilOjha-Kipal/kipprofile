from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

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
        if request.method == 'POST':
        
            a=int(request.POST['n1'])
            b= int(request.POST['n2'])
        
            op = a+b
            # return HttpResponseRedirect('/form') #this is used for redirect by using django.http
            # return redirect('/') #this is used for redirect by using django.shortcut
    except:
        print('not calculate')
    return render(request,'form.html', {'output' : op } )

def submit(request):
    return HttpResponse(request)
   
def cal(request):
    try:
           if request.method == 'POST':
        
            a=int(request.POST['n1'])
            b= int(request.POST['n2'])
            c=request.POST["oper"]
        
            op = acb
            # return HttpResponseRedirect('/form') #this is used for redirect by using django.http
            # return redirect('/') #this is used for redirect by using django.shortcut
    except:
        print('not calculate')
    return render(request,'form.html', {'output' : op } )