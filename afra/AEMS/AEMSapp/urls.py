from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    path('',views.index, name='index'),
     path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('empapplyleave',views.empapplyleave, name='empapplyleave'),
    path('empleave',views.empleave, name='empleave'),
    path('empattendance',views.empattendance, name='empattendance'),
    path('empexpdetails',views.empexpdetails, name='empexpdetails'),
    path('empinfo',views.empinfo, name='empinfo'),
    path('emppayroll',views.emppayroll, name='emppayroll'),
    path('empshift',views.empshift, name='empshift'),
    path('new1',views.new1, name='new1'),
    path('new2',views.new2, name='new2')
    
]