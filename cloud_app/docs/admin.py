from django.contrib import admin

from .models import Operator, Document, Planet, Character

# Register your models here.
admin.site.register(Operator)
admin.site.register(Document)
admin.site.register(Planet)
admin.site.register(Character)
