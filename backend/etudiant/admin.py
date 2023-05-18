from django.contrib import admin

# Register your models here.
from .models import Etudiant, Prop, Anno
admin.site.register(Etudiant)
admin.site.register(Prop)
admin.site.register(Anno)
