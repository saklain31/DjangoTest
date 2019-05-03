# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from table_test.models import * 
from table_test.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.



def send(request):
    p = Publisher(name='who am I', city='Berkeley')
    p.save()
    return HttpResponse((p.city,p.name))


def submitOrder(request):
    order = Order()
    order.orderID = 'ord4'
    order.userID = 'user123'
    order.address1 = 'amaraddress11'
    order.address2 = 'amaraddress12'
    order.save()
    return HttpResponse('mone hoy save hoise')

def setMeasurements(request):
    mes = Measurements()
    mes.orderID = 'ord456'
    mes.jeans1 = 'myjeans1'
    mes.thread1 = 'mythread1'
    mes.save()
    return HttpResponse(mes)


def printOrder(request):
    order_list = Order.objects.exclude(orderID='ord2')

    #return HttpResponse(order_list[1].orderID)
    return render(request, 'tablePrint.html',{'messages': order_list})



def index(request):
    return render(request,'table_test/index.html')
@login_required

def special(request):
    return HttpResponse("You are logged in !")
@login_required

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'table_test/login.html', {})
