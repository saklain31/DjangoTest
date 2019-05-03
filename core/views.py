# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from core.forms import SignUpForm

def sign_up(request):
    print("koi?")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #username = form.cleaned_data.get('username')
        #raw_password = form.cleaned_data.get('password1')
	#username = form.cleaned_data.get('email')
        #print(username,email)
	print(form.is_valid())
        if form.is_valid():
            print("vitore")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username)
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse("signed up")
            
    else:
        form = SignUpForm()	

    return render(request, 'signup.html', {'form': form, 'msg': 'Invalid Information'})
