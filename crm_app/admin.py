from django.contrib import admin
from . models import Leads,CustomUser,AdminHOD,Agent

# Register your models here.

# admin.site.register(Profile)
admin.site.register(Leads)
admin.site.register(CustomUser)
admin.site.register(AdminHOD)
admin.site.register(Agent)
