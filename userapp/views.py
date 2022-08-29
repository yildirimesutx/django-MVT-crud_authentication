from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "userapp/home.html")


def special(request):
    return render(request, "userapp/special.html")    
