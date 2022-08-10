from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("<h1 style='text-align:center;'>Django Developer</h1>")    
