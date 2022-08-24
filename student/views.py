from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def new(request):
    return render(request, "student/index.html")



def student(request):
    print(request.POST)
    form = StudentForm()
    context = {
      "form": form
   }


    return render(request, "student/student.html", context)
