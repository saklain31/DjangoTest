# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect



# Create your views here.
def signup(request):
    if request.method == 'POST':
		username = request.POST.get("email")
		psw = request.POST.get("psw")
		user = User.objects.create_user(username=username,email=username,password=psw)
		user.lastname = "lol"
		user.save()




    return render(request, 'sign.html')

# def signup(request):
#     if request.method == 'POST': 
#         if form.is_valid():  
#             return HttpResponse(form.cleaned_data['email']) # Redirect after POST
#     else:
#         return HttpResponse('GET REQ ASHCHE')

#     return render('sign.html', {
#         'form': form
#     })
