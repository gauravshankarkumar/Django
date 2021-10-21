from django.shortcuts import render , redirect
# from django.contrib.auth import authenticate , logout
from django.contrib import auth



# Create your views here.
def logout (request):
    print("louout")
    auth.logout(request)
    print("1")
    return redirect('/')