from django.shortcuts import render
from django.http import request, HttpResponse
from django.views import View
from . import views

# Create your views here.


def index(request):
    return render(request,'firstpage.html',{"testvar":'fungerar'})

def about(request):
    return render(request,'about.html')

def tickets(request):
    return render(request,'tickets.html')

def ml(request):
    return render(request,'ml.html')