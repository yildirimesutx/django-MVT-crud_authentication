from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout, login, authenticate

from django.contrib import messages



def home(request):
    return render(request, 'customize_user/home.html')


def user_logout(request):
    messages.success(request, "You logged out!")
    logout(request)
    return redirect("home")