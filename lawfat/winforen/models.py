from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


class registrationModel(models.Model):
    first_name = models.CharField(max_length = 128)
    last_name  = models.CharField(max_length = 128)
    email      = models.EmailField(max_length = 256, unique = True)
    verify_email = models.EmailField(max_length = 256)



