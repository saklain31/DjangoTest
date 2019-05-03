# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from table_test.models import *

admin.site.register(Publisher)
admin.site.register(Order)
admin.site.register(Measurements)
admin.site.register(User)
admin.site.register(UserProfileInfo)

