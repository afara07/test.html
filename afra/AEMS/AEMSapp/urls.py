from turtle import update
from django.urls import path
from django.views import View
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    path('',views.index, name='index'),
    path('test',views.machinetest,name='test'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('empapplyleave',views.empapplyleave, name='empapplyleave'),
    path('empleave',views.empleave, name='empleave'),
    path('empattendance',views.empattendance, name='empattendance'),
    path('empexpdetails',views.empexpdetails, name='empexpdetails'),
    path('empinfo',views.empinfo, name='empinfo'),
    path('insertinfo',views.info_details, name='insertinfo'),
    path('view_information',views.view_details, name='view_information'),
    path('emppayroll',views.emppayroll, name='emppayroll'),
    path('empshift',views.empshift, name='empshift'),
    path('new1',views.new1, name='new1'),
    path('new2',views.new2, name='new2'),
    path('details',views.show_details, name='details'),
    path('delete_data/<int:id>',views.delete, name='delete'),
    path('product',views.shop_details, name='product'),
    path('product_det',views.product_details, name='product_det'),
    path('delete_data1/<int:id>',views.delete_product, name='delete_data1'),
    path('update/<int:id>',views.update, name='update'),
    path('updated_data/<int:id>',views.edit, name='updated_data'),
    path('signup',views.signup_form, name='signup'),
    path('login1',views.login_form, name='login1'),
    path('admin',views.admin_page, name='admin'),
    path('department',views.department_add, name='department'),
    path('department_view',views.department_details, name='department_view'),
    path('view',views.view_profile, name='view'),
    path('log_out',views.log_out, name='log_out'),
    path('check_exist',views.check, name='check_exist'),
    path('new_form',views.form1, name='new_form'),
    path('form',views.form, name='form'),
    path('info_delete',views.info_edit, name='info_delete'),
    path('update_info',views.update_information, name='update_info'),
    path('api',views.api_integration, name='api'),
    path('api/<int:id>',views.api_integration, name='api'),
    path('delete_department',views.delete_depart, name='delete_department'),
    path('update_department',views.update_depart, name='update_department'),
    path('check_exist1',views.exist, name='check_exist1')


   ]