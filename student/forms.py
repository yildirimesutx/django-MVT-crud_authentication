from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
     class Meta:
        model = Student
        fields = "__all__"
        # fields = ["first_name", "last_name"]
        # labels = {"last_name" : "Surname"} labels değiştirebiliyoruz
