from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('congratulations you have created a web application')
def home1(request):
    return render(request, 'home1.html')

# Create your views here.
