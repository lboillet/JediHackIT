from django.db import models

# Create your models here.
class Student(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    percentage = models.CharField(max_length=200)
    payment = models.CharField(max_length=200)
