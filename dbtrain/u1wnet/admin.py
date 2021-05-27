from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *





class Un1modelAdmin(admin.ModelAdmin):
    fields = ['name', 'version']

admin.site.register(Un1model, Un1modelAdmin)



