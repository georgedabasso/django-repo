from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('home/', views.home, name="home"),
    path('referrals/', views.referrals, name="referrals"),
    path('products/', views.getproducts, name="myproducts"),
    path('orders/', views.orders, name="orders"),
    path('my_template/', views.my_template, name="my_template"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name='registration'),
    path('adduser', views.adduser, name='addinguser'),


    path('adduser', views.adduser, name='addinguser'),


    path('edituser/<id>', views.edituser, name='edituser'),
    path('updateuser/<id>', views.updateuser, name='updateuser'),
    path('deleteuser/<id>', views.deleteuser)
]