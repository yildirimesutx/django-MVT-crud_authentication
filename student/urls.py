from django.urls import path
from .views import new,student

urlpatterns = [
    path('new', new ),
    path('s/', student ),
  
]