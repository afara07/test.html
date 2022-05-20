from django.urls import path
from django.views import View
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 


urlpatterns = [
    path('',views.index, name='index'),
    path('department_page',views.department, name='department_page'),
    path('add_employee',views.add, name='add_employee'),
    path('view_page',views.view_employe, name='view_page'),
    path('viewsalary',views.sal, name='viewsalary'),
    path('payroll',views.payroll_calculation, name='payroll')


]