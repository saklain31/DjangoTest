# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60)

class Order(models.Model):
	orderID = models.CharField(max_length=30)
	userID = models.CharField(max_length=30)
	address1 = models.CharField(max_length=60)
	address2 = models.CharField(max_length=60)
	payment = models.CharField(max_length=30)
	status = models.CharField(max_length=30)

class Measurements(models.Model):
	orderID = models.CharField(max_length=30)
	jeans1 = models.CharField(max_length=30)
	thread1 = models.CharField(max_length=30)
	jeans2 = models.CharField(max_length=30)
	thread2 = models.CharField(max_length=30)
	tailor1 = models.CharField(max_length=30)
	tailor2 = models.CharField(max_length=30)
	tailor3 = models.CharField(max_length=30)

class User(models.Model):
	userID = models.CharField(max_length=30) 
	gmail = models.EmailField()
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=30)
	address1 = models.CharField(max_length=60)
	address2 = models.CharField(max_length=60)
	city = models.CharField(max_length=30)

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	#profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
 	
 	def __str__(self):
         return self.user.username