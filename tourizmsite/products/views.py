from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def products(request):
     return render(request,'products/products.html')

def customer(request):
     return render(request,'products/customer.html')

def dashboard(request):
     return render(request,'products/dashboard.html')
