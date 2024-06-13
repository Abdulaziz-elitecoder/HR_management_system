from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Employee(AbstractUser):
    email = models.EmailField(unique=True)
    is_hr = models.BooleanField(default=False)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
