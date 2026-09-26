from django.shortcuts import render, redirect
from authApp.models import UserModel



def login_view(request):


    return render(request, 'login.html')

