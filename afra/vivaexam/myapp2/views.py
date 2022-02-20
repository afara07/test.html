from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("congratulation you are on")
def login(request):
    return render(request, 'login.html')  
def admin(request):
    return render(request, 'admin.html')
def home(request):
    return render(request, 'home.html')   
def student(request):
    return render(request, 'student.html')
def master(request):
    return render(request, 'master.html') 
def demo(request):
    return render(request, 'demo.html')             
def viva(request):
    return render(request, 'viva.html')             