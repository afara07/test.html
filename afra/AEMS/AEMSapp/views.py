from ast import Return
from distutils.log import info
import email
import re
from telnetlib import LOGOUT
from tkinter import Place
from tkinter.tix import Form
from unicodedata import name
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from AEMSapp.serializers import UserSerializer
from . models import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

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

@csrf_exempt 
def info_details(request):
    name = request.POST['name']
    password = request.POST['password']
    mail = request.POST['email']
    dob = request.POST['DOB']
    doj = request.POST['DOJ']
    depart = request.POST['department']
    mob = request.POST['mobile_number']
    gen = request.POST['gender']
    print(name,password,mail,dob,doj,depart,mob,gen)
    informtion=Info(name=name,password=password,email=mail,DOB=dob,DOJ=doj,department=depart,mobile_number=mob,gender=gen)
    informtion.save()
    return JsonResponse({'message': 'successfully enterded the details'})

def view_details(request):
    insert_info=Info.objects.all()
    return render(request, 'viewinfo.html',{"data":insert_info})

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

def show_details(request):
    details=Employees.objects.all()
    return render(request, 'new3.html',{"data":details}) 

def delete(request,id):
    print (id)
    Employees.objects.get(id=id).delete()
    return redirect('details')

def shop_details(request):
    if request.method=="POST":
        nam=request.POST['product_name']
        dcrptn=request.POST['product_details']
        price=request.POST['price']
        print(nam,dcrptn,price)
        full_details=Products(product_name=nam,product_details=dcrptn,price=price)
        full_details.save()
    return render(request, 'shop.html')

def product_details(request):
    product_info=Products.objects.all()
    return render(request, 'shop1.html',{"data":product_info}) 

def delete_product(request,id):
    print(id)
    Products.objects.get(id=id).delete()
    return redirect('product_det')

def update(request,id):
    print(id)
    update_details=Employees.objects.get(id=id)
    return render(request, 'update.html',{"data":update_details})

def edit(request,id):
    print(id)
    if request.method=="POST":
        updated_name=request.POST['name']
        updated_address=request.POST['address']
        updated_place=request.POST['place']
        updated_salary=request.POST['salary']
    Employees.objects.filter(id=id).update(employe_name=updated_name,address=updated_address,place=updated_place,salary=updated_salary)
    return redirect('details')

def signup_form(request):
    if request.method=='POST':
        nam=request.POST['username']
        mail=request.POST['email']
        password=request.POST['password']
        user_details=Register(username=nam,email=mail,password=password)
        user_details.save()
    return render(request, 'signup.html')

def login_form(request):
    if request.method=='POST':
        email=request.POST['mail']
        password=request.POST['password']
        try:
            login_details=Register.objects.get(email=email)
            print(login_details.password)
            print(login_details.email)
            # print(login_details.username)
            if login_details.email==email and login_details.password==password:
                request.session['loged_user']=login_details.id
                print(request.session['loged_user'])
                return redirect('admin')
            else:
                return render(request,'login1.html',{'msg':"login failed"})
        except Register.DoesNotExist:
            return render(request,'login1.html',{'msg':"login failed"})
    return render(request, 'login1.html')
def view_profile(request):
    try:
        active_session=request.session['loged_user']
        active_user=Register.objects.get(id=active_session)
        return render(request, 'view_profile.html',{'data':active_user})
    except Exception:
        return render(request, 'login1.html')
def log_out(request):
    # logout(request)
    request.session.flush()
    return redirect('login1')
@csrf_exempt
def check(request):
    email=request.POST['email_id']
    print(email)
    exist_user=Register.objects.filter(email=email).exists()
    return JsonResponse({'isExist':exist_user})

def admin_page(request):
    return render(request, 'admin.html')

def department_add(request):
    if request.method=="POST":
     nam=request.POST['name']
     dcrptn=request.POST['description'] 
     print(nam,dcrptn)
     department_view=Department(name=nam,description=dcrptn)
     department_view.save()   
    return render(request, 'department.html')

def department_details(request):
    depart=Department.objects.all()
    return render(request, 'department_view.html',{"data":depart})

def form1(request):
    return render(request, 'form1.html')

def form2(request):
    return render(request, 'form.html')

@csrf_exempt   
def form(request):
   

    name=request.POST['name']
    address=request.POST['address']
    place=request.POST['place']
    age=request.POST['age']
    print(name,address,place,age)
    form_details=forms(name=name,address=address,place=place,age=age)
    form_details.save()
    return JsonResponse({'message':'details added successfully'})

@csrf_exempt 
def info_edit(request):
    userid=request.POST['id']
    delete_data=Info.objects.get(id=userid).delete()

    return JsonResponse({'message':'data deleted successfully'})
    
@csrf_exempt
def update_information(request,id):
    info_new=request.POST['id']
    update_data=Info.objects.get(id=id).update()
    return JsonResponse({'meassage':'data updated suuccessfully'})   

@csrf_exempt
def api_integration(request,id=0):
    if request.method=='POST':
        user_data= JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({'meassage':'data inserted successfully'})
        return JsonResponse({'message':'data insertion failed'})

   

    elif request.method=='GET':
        user = Register.objects.all()
        user_serializer = UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False)

    elif request.method=='DELETE':
        print('------')
        print(id)
        user_delete = Register.objects.get(id=id)
        user_delete.delete()
        
        return JsonResponse({'message':'data deleted'})

    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user_update = Register.objects.get(id=user_data['id'])
        user_serializer = UserSerializer(user_update,user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({"message":"data updated successfully"})
        return JsonResponse({"message":"data updated failed"})

def delete_depart(request,id):
    Department.objects.get(id=id).delete()
    return redirect('delete_department')



def update_depart(request,id):
     update_departinfo = Department.objects.get(id=id)
     return render(request, 'department_update.html',{"data":update_departinfo})

@csrf_exempt
def exist(request):
    name=request.POST['name']
    Exist_user=forms.objects.filter(name=name).exists()
    print(name)
    return JsonResponse({'message':Exist_user})

def machinetest(request):
    return render(request, 'test.html')
    





# # Create your views here.

