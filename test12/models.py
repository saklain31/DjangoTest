# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



# class Event(models.Model):
#     name = models.CharField('Event Name', max_length=120)
#     event_date = models.DateTimeField('Event Date')
#     venue = models.CharField(max_length=120)
#     manager = models.CharField(max_length = 60)
#     description = models.TextField(blank=True)


# class Publisher(models.Model):
#     name = models.CharField(maxlength=30)
#     address = models.CharField(maxlength=50)
#     city = models.CharField(maxlength=60)
#     state_province = models.CharField(maxlength=30)
#     country = models.CharField(maxlength=50)
#     website = models.URLField()

# class Author(models.Model):
#     salutation = models.CharField(maxlength=10)
#     first_name = models.CharField(maxlength=30)
#     last_name = models.CharField(maxlength=40)
#     email = models.EmailField()
#     headshot = models.ImageField(upload_to='/tmp')

# class Book(models.Model):
#     title = models.CharField(maxlength=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()