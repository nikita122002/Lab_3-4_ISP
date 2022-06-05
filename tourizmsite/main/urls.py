from django.contrib.auth import login
from django.urls import path
from . import views
from .views import register,login

urlpatterns =[

    path('', views.home),
    path('register/',register,name='register'),
    path('login/',login,name='login')

]