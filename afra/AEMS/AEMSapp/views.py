import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def index(request):
    return HttpResponse("congratulations you are created a project")
def home(request):
    return render (request, 'home.html')     
def login(request):
    return render (request, 'login.html') 
def empapplyleave(request):
    return render (request, 'empapplyleave.html') 
def empleave(request):
    return render (request, 'empleave.html')
def empattendance(request):
    return render (request, 'empattendance.html') 
def empexpdetails(request):
    return render (request, 'empexpdetails.html')  
def empinfo(request):
    return render (request, 'empinfo.html') 
def emppayroll(request):
    return render (request, 'emppayroll.html') 
def empshift(request):
    return render (request, 'empshift.html') 
def new1(request):
    return render (request, 'new1.html')
def new2(request):
    if request.method=="POST":
        nam=request.POST['name']
        add=request.POST['address']
        pla=request.POST['place']
        sal=request.POST['salary']
        print(nam,add,pla,sal)
        employee_details=Employees(employe_name=nam,address=add,place=pla,salary=sal)
        employee_details.save()
    return render(request, 'new2.html')                      
# Create your views here.
