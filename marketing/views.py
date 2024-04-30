from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader #for routing your templates
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import user
from .models import products
from .serializers import productsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
   data=user.objects.all()
   context= {'data':data}
   return render(request, 'registration.html', context)

@csrf_exempt
def adduser(request):
   if request.method == 'POST':
    formname = request.POST.get('fullname')
    formemail = request.POST.get('email')
    formpassword = request.POST.get('password')

    obj1=user(fullname=formname,email=formemail,password=formpassword)
    obj1.save()

    #fetch the student data to be displayed

    mydata = user.objects.all()
    context = {'data': mydata}

    return render(request, 'registration.html', context)


def edituser(request,id):
      data = user.objects.get(id=id);
      context ={'data': data}
      return render(request, 'updateuser.html',context)

def updateuser(request,id):
    if request.method == 'POST':
        formname = request.POST.get('fullname')
        formemail = request.POST.get('email')
        formpassword = request.POST.get('password')


        #modifying the student details based on the student id given
        edituser = user.objects.get(id=id)#here i fetch the student to be changed
        edituser.fullname = formname
        edituser.email = formemail
        edituser.password = formpassword
        #save the changes
        edituser.save()
        #display the new changes in html table to fetch them from the database table
        data = user.objects.all()
        #i create a dictionary to hold the fetched info
        context = {'data': data}
        #pass the fetched info back to the dashboard
    return render(request, 'registration.html',context)

def deleteuser(request,id):
    deleteuser = user.objects.get(id=id)
    deleteuser.delete()
    return redirect('/registration')


@api_view(['GET','POST'])
def getproducts(request,format=None):
        if request.method == 'GET':
            prod= products.objects.all()
            serializer = productsSerializer(prod,many=True)
            return Response(serializer.data)



