from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("<h1 style='text-align:center;'>Django Developer</h1>")

def special(request):
    
    context = {
      "title":"django developer",
      "my_list":[2,3,4],
      "dict1": {"django":"best framework"}
     
    }

    return render(request, "app/special.html", context)         
