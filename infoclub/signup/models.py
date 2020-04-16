from django.db import models
from django import forms
#from signup.registration_form import regForm

# Create your models here.

class regModel(models.Model):
    first_name = models.CharField(max_length = 128) 
    last_name = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 256, unique = True)
    verify_email = models.EmailField(max_length = 256, unique = True)

'''
Error coding: will be deleted after implementing in form
#Importing all fields from the registration_form.py
class regModel(models.Model):
    class Meta():
        model = regForm
        fields = models.exclude('botcatcher', 'verify_email')
'''
