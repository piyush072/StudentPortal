from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Name(models.Model):
    Full_Name = models.CharField(null=True,max_length=40)

class Semester(models.Model):
    Semester = models.CharField(max_length=3)

class CustomUser(AbstractUser):
    Full_Name = models.ForeignKey(Name, null=True, on_delete=models.CASCADE)
    Semester = models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.email
