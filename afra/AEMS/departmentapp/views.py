import email
import re
from telnetlib import LOGOUT
from tkinter import Place
from unicodedata import name
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from . models import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("congratulations you are created a project")


def department(request):
    return render(request, 'home2.html')

@csrf_exempt
def add(request):
    if request.method=="POST":
     last = request.POST["employee_name"]
     adres = request.POST["address"]
     age = request.POST["age"]
     gender = request.POST["gender"]
     contact = request.POST["mobile"]
     mail = request.POST["email"]
     date = request.POST["dob"]
     place=request.POST["place"]
     print(last)
     added=Employee_add(employee_name=last,address=adres,age=age,gender=gender,mobile=contact,email=mail,dob=date,place=place)
     added.save()
    return render(request, 'add.html')

    

def view_employe(request):
    employee_insert =Employee_add.objects.all() 
    return render(request, 'view.html',{"data":employee_insert})


def sal(request):
    return render(request, 'viewsal.html')

def payroll_calculation(request):
    if request.method=="POST":
        nam = request.POST['emp_name']
        basicpay = request.POST['basic_pay']
        hra = request.POST['HRA']
        ta = request.POST['TA']
        da = request.POST['DA']
        it = request.POST['IT']
        pf = request.POST['PF']
        createsal = request.POST['Gross_salary']
        net = request.POST['Net_salary']
        insert = Payroll(emp_name=nam,basic_pay=basicpay,HRA=hra,TA=ta,DA=da,IT=it,PF=pf,Gross_salary=createsal,Net_salary=net)
        insert.save()
    return render(request, 'creatsal.html')


# Create your views here.
