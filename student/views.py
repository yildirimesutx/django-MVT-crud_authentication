from django.shortcuts import render, redirect
from .forms import StudentForm

# Create your views here.

def new(request):
    return render(request, "student/index.html")



def student(request):
    print(request.POST)

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("news")
    context = {
      "form": form
   }


    return render(request, "student/student.html", context)
