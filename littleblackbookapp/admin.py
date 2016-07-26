from django.contrib import admin

# Register your models here.

from .models import Professional, Company, Strengths

admin.site.register(Professional)
admin.site.register(Company)
admin.site.register(Strengths)
