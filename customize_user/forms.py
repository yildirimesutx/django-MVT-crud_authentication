from django.contrib.auth.models import User
from .models import UserProfile

from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User # user ı kullan ve sadece username ve email aldık
        fields= ('username', 'email')

class UserProfileForm(forms.ModelForm):   #burada hazır modelden form ürettik
    class Meta:
        model = UserProfile
        exclude = ('user',)    #tek elemanınlı tupple kullandığımız için sonuna , k      