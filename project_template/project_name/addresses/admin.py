# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Address, City, Country

# Register your models here.

admin.site.register(Address)
admin.site.register(City)
admin.site.register(Country)

