# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Customer, Inventory, Rental, Payment, Staff,  Store

# Register your models here.
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Rental)
admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(Store)
