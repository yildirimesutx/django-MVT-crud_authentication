from django.db import models

# django default user modelini import ettik 
from django.contrib.auth.models import User



class UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pic", blank=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # django default user modelini import ettik oluşturduğumuz model ile one to one olacak şekilde ilişkilendirdik
    def __str__(self):
        return f"{self.user.username}"
