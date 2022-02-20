from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('admin',views.admin, name='admin'),
    path('home',views.home, name='home'),
    path('student',views.student, name='student'),
    path('master',views.master, name='master'),
    path('demo',views.demo, name='demo'),
    path('viva',views.viva, name='viva')
]