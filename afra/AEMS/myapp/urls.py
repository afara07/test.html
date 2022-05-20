from unicodedata import name
from django.urls import path
from django.views import View

from departmentapp.models import Payroll
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index, name='index'),
    path('employee_page',views.employee, name='employee_page'),
    path('profile',views.profile_details, name='profile')
    
    
]
