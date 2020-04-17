from django.db import models
#from django import forms
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #Additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username

'''
class regModel(models.Model):
    first_name = models.CharField(max_length = 128) 
    last_name = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 256, unique = True)
    verify_email = models.EmailField(max_length = 256, unique = True)
'''



'''
Error coding: will be deleted after implementing in form
#Importing all fields from the registration_form.py
class regModel(models.Model):
    class Meta():
        model = regForm
        fields = models.exclude('botcatcher', 'verify_email')
'''
