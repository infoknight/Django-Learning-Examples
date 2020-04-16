from django.db import models

# Create your models here.
class signupModel(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name  = models.CharField(max_length = 128)
    email      = models.EmailField(max_length = 256, unique = True)
    verify_email = models.EmailField(max_length = 256)



