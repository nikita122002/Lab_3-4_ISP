from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm, ContactForm
from .models import TourizmType, TourPlace, Category, Shop
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'main/home.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'nikzxc98@mail.ru',
                             ['nik122002@outlook.com'], fail_silently=False)
            if mail:
                logger.info(request, 'Письмо отправлено')
                return redirect('home')
            else:
                logger.error(request, 'Ошибка отправки')
        else:
            logger.error(request, 'Ошибка регистрации')

    else:
        form = ContactForm()
    return render(request, 'main/feedback.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            logger.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {"form": form})


def tourtype(request):
    tourtype = TourizmType.objects.all()
    return render(request, 'main/tourtype.html', {'tour': tourtype})


def tourplace(request):
    tourplace = TourPlace.objects.all()
    categories = Category.objects.all()
    context = {
        'place': tourplace,
        'categories': categories,
    }
    return render(request, 'main/tourplace.html', context=context)


def get_category(request, category_id):
    categ = TourPlace.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'main/category.html', {'categ': categ, 'categories': categories, 'category': category})


def view_tourplace(request, category_id):
    tourplace_item = TourPlace.objects.get(pk=category_id)
    return render(request, 'main/view_tourplace.html', {"tourplace_item": tourplace_item})


def shop(request):
    shop = Shop.objects.all()
    return render(request, 'main/shop.html', {'shop': shop})
