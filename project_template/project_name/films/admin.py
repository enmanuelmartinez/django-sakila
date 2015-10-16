# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Actor, Category, Film, Language

# Register your models here.

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Language)

