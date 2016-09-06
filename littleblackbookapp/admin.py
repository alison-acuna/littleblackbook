from django.contrib import admin

# Register your models here.

from .models import Professional, Company, Strengths, Post


admin.site.register(Professional)
admin.site.register(Company)
admin.site.register(Strengths)
admin.site.register(Post)


#  from .models import PinFeed, UserPinFeed, PinManager
#
# admin.site.register(PinFeed)
# admin.site.register(UserPinFeed)
# admin.site.register(PinManager)
