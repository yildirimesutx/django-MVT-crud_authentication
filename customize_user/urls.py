from django.urls import path
from .views import home, user_logout, register, user_login

urlpatterns = [
    path('', home, name="home"),
    path('logout/', user_logout, name="logouts"),
    path('register/', register, name="register"),
    path('login/', user_login, name="logins"),
  
]