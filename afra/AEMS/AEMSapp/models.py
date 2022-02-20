from django.db import models


# Create your models here.
class Employees(models.Model):
    employe_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    salary = models.IntegerField()
    
      