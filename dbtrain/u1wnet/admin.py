from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *





class U1modelAdmin(admin.ModelAdmin):
    fields = ['name', 'version']

admin.site.register(Un1model, U1modelAdmin)



