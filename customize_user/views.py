from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout, login, authenticate

from django.contrib import messages
from .forms import UserForm, UserProfileForm 






def home(request):
    # messages.success(request, 'home page')
    
    return render(request, 'customize_user/home.html')


def user_logout(request):
    
    
    logout(request)
    messages.success(request, 'You logged out!')
    redirect("home")
    
    return render(request, 'customize_user/home.html')



def register(request):
    form_user = UserForm()
    form_profile =UserProfileForm()

    messages.success(request, 'register succesful')
    print(request.POST)
    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }

    return render(request, "customize_user/register.html", context)



