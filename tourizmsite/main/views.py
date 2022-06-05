from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import UserRegisterForm,UserLoginForm


def home(request):
    return render(request,'main/home.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect ('home')
        else:
            messages.error(request,'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    return render(request,'main/register.html',{"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request,'main/login.html',{"form": form})