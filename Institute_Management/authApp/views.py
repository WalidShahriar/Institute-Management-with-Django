from django.shortcuts import render, redirect
from authApp.models import UserModel
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    form_data = AuthenticationForm()

    context = {
        'form_data' : form_data
    }

    return render(request, 'login.html', context)

def logout_view(request):

    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('login_view')

