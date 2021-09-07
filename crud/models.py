from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + " " + self.gender
