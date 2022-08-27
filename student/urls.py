from django.urls import path
from .views import home, student, student_list, student_add, student_update, student_delete

urlpatterns = [
    path('', home, name="news"),
    path('new', student ),
    path("list", student_list, name="list"),
    path("add", student_add, name="add"),
    path("update/<int:id>", student_update, name="update"),
    path("delete/<int:id>", student_delete, name="delete")
  
]