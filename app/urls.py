
from django.urls import path
from .views import home, about, special


urlpatterns = [
  
    path("home/", home, name="home"),
    path("about/",about , name="about"),
    path("special/", special, name="special")
]