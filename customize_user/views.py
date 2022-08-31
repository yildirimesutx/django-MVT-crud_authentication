from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import logout, login, authenticate

from django.contrib import messages
from .forms import UserForm, UserProfileForm 

from django.contrib.auth.forms import AuthenticationForm






def home(request):
    # messages.success(request, 'home page')
    
    return render(request, 'customize_user/home.html')


def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('home')



    # messages.success(request, 'You logged out!')
    # logout(request)
    
    # # redirect("home")
    
    # return render(request, 'customize_user/home.html')



def register(request):
    form_user = UserForm()
    form_profile =UserProfileForm()

    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_profile =UserProfileForm(request.POST, request.FILES)
        #form_profile da dosya yüklemem islemi oldugundan dolayı, yuklenen dosyayı Post ile değil request.FILES ile alıyoruz

        if form_user.is_valid() and form_profile.is_valid():
            users = form_user.save()
            profile =form_profile.save(commit=False)
            #yukarıdaki form_user save işlemi yapıyor fakat form_profile hangi user a kaydedeceğini bilmiyor ve hata veriyor,user fieldini forms.py da exclude ile ayırmıştık, sebebi form sayfasında tüm user listesini verdiğinden dolayı user fieldi istemedik, save(commit=False) bize formdan bilgileri al fakat DB kaydetme için kullandık, bilgileri aldık ve ilgili user ı da from_profile kaydederek en son save() işlemini yaptık.
            profile.user = users
            profile.save()

            login(request, users)
            messages.success(request, 'register succesful') 
            return redirect("home")
       



 
    
    context = {
        "form_user": form_user,
        "form_profile": form_profile
    }

    return render(request, "customize_user/register.html", context)




def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        # username = form.cleaned_data('username')
        # password = form.cleaned_data('password')

        # user = authenticate(username=username, password=password)
     
        #yukarıdaki uç satır için get_user tek başına yeterli


        user = form.get_user()

        if user:
           messages.success(request, 'login succesful')
           login(request, user)
           return redirect("home")

    return render(request, "customize_user/user_login.html", {"form":form} )     




