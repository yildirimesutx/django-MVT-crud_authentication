from django.shortcuts import render, redirect


#register icin formu aldık
from django.contrib.auth.forms import UserCreationForm

# register olduktan sonra login olması için 
from django.contrib.auth import authenticate, login



def home_view(request):
    return render(request, "userapp/home.html")


def special(request):
    return render(request, "userapp/special.html")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
        #    return redirect("login")
    # bu bölüma kadar olan kısımda register islemi tamam bundan sonraki kisim register olduktan sonra login olmak maksadıyla 

           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get("password1")


           user = authenticate(username=username,
          password=password)
           login(request, user)
           return redirect("home") 

    
    context = {
        "form":form
        }

    return render(request, "registration/register.html", context)


