from statistics import mode
from django.db import models


# Create your models here.

class Employee_add(models.Model):
   employee_name = models.CharField(max_length=50)
   address = models.CharField(max_length=50)
   age = models.IntegerField()
   gender = models.CharField(max_length=50)
   mobile = models.IntegerField()
   email = models.EmailField(max_length=50)
   dob = models.DateField()
   place = models.CharField(max_length=50)

class Payroll(models.Model):
   emp_name = models.CharField(max_length=50)
   basic_pay = models.IntegerField()
   HRA = models.IntegerField()
   TA = models.IntegerField()
   DA = models.IntegerField()
   IT = models.IntegerField()
   PF = models.IntegerField()
   Gross_salary = models.IntegerField()
   Net_salary = models.IntegerField()