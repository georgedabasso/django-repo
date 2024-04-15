from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('referrals/', views.referrals, name="referrals"),
    path('products/', views.products, name="products"),
    path('orders/', views.orders, name="orders"),
    path('my_template/', views.my_template, name="my_template"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
    path('adduser/', views.adduser, name="addinguser")

]