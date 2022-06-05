from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm


def home(request):
    return render(request,'main/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегистрировались')
            return redirect ('login')
        else:
            messages.error(request,'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    return render(request,'main/register.html',{"form": form})

def login(request):
    return render(request,'main/login.html')