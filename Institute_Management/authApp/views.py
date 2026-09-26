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

    if request.method == 'POST':
        form_data = AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                messages.success(request, "Successfully Logged-In!")
                return redirect('dashboard')

    return render(request, 'login.html', context)

@login_required
def logout_view(request):

    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('login_view')

