from django.contrib import admin
from .models import CustomUser, Proprietaire, Etudiant

admin.site.register(CustomUser)
admin.site.register(Proprietaire)
admin.site.register(Etudiant)
