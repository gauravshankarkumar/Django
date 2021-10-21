# from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib import auth

# Create your views here.
def login (request):
    if request.method=="POST":
        username1= request.POST ['username']
        password1= request.POST ['password']

        # authenticate.login(request.user)
        from django.contrib import auth
        user =auth.authenticate (username=username1,password=password1)
        print("ok")
        if user is not None:
            print("not none")
            auth.login(request, user)
            print("user loged")
            return redirect('/')
        
           
        else:
            print("wrong password")
            return redirect('http://127.0.0.1:8000/app3/login')
                

    else:
        print("html")
        return render (request, 'login.html')
        