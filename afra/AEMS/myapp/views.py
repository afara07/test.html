from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("congratulations you are created a project")

def employee(request):
    return render(request, 'page2.html') 

def profile_details(request):
    return render(request, 'profile.html')

  
# Create your views here.
