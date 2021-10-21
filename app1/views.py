from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def home (request):
    return render(request, 'home.html',{'title':'Home Page','button':'Profile','link':'/profile'})

def profile (request):
    return render(request, 'home.html',{'title':'Profile Page','button':'Home','link':'/'})

def form (request):
    return render(request, 'form.html',{'title':'Form Page','button':'Home','link':'/'})

def expression (request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request, 'output.html',{'result':c ,'button':'Home','link':'/'})


