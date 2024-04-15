from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #for routing your templates

from marketing.models import user


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())

def referrals(request):
    template = loader.get_template('referrals.html')
    return HttpResponse(template.render())

def orders(request):
    template = loader.get_template('orders.html')
    return HttpResponse(template.render())

def my_template(request):
    template = loader.get_template('my_template.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())

def adduser(request):
    if request.method == 'post':
        Fullname= request.post.get['fullname']
        Email= request.post.get['email']
        Password= request.post.get['password']

        obj1=User(Fullname=Fullname,Email=Email)
        obj1.save()

    #fetch the student data to be displayed
    data = user.objects.all();
    context = {'data': data}
    return render(request, 'registration.html', context)