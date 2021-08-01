from django.contrib import admin

from .models import  DataUpdate, Planet, Character

# Register your models here.
admin.site.register(DataUpdate)
admin.site.register(Planet)
admin.site.register(Character)
