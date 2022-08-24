from django.urls import path
from .views import new,student

urlpatterns = [
    path('new/', new, name="news"),
    path('s/', student ),
  
]