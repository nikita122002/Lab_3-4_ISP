from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def create(request):
     return render(request,'products/create.html')

def customer(request):
     return render(request,'products/customer.html')
