from django.contrib import admin

# Register your models here.

from .models import Professional, Company

admin.site.register(Professional)
admin.site.register(Company)
