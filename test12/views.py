# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *

def index1(request):
    return render(request, 'form.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('email', None)
        try:
            user = search_id
            #do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'form.html')
