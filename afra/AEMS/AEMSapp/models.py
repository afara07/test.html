from statistics import mode
from django.db import models


# Create your models here.
class Employees(models.Model):
    employe_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    salary = models.IntegerField()

class Products(models.Model):
     product_name = models.CharField(max_length=50)
     product_details = models.CharField(max_length=200)
     price = models.IntegerField()

class Register(models.Model):
      username = models.CharField(max_length=50)
      email = models.EmailField(max_length=50)
      password= models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class forms(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    age = models.IntegerField()

class Info(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    DOB = models.DateField()
    DOJ = models.DateField()
    department = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    gender = models.CharField(max_length=10)

    


