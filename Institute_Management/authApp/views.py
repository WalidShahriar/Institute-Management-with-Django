from django.shortcuts import render, redirect
from authApp.models import UserModel
from django.contrib.auth import login, logout
from django.contrib import messages


def login_view(request):


    return render(request, 'login.html')

def logout_view(request):

    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('login_view')

