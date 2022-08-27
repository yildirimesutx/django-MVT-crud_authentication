from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.

#sayfayı render etmek için kullanıldı
def home(request):
    return render(request, "student/index.html")


# oluşturduğumuz form sayfası aracılığı ile student eklendi
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


#----------------CRUD-----------------#

#read(GET)

def student_list(request):
    student = Student.objects.all()

    context = {
        'student' : student,
    }

    return render(request, "student/student_list.html", context)




# create(POST)


def student_add(request):
    # form = StudentForm()
    # if request.method == "POST":
    #     print(request.POST)
    form = StudentForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect("list")


    context = {
        "form" : form
    }

    return render(request, "student/student_add.html", context) 



# Update (POST)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        "form" :form
    }

    return render(request, "student/student_update.html", context)  


# Delete (POST) 


def student_delete(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()

        messages.success(request, "Student deleted successfully")
        return redirect("list")

    return render(request, "student/student_delete.html")    






