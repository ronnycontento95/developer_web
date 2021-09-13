from django.contrib.admin.sites import site
from perfil.models import Hobbies, Perfil
from django.contrib import admin
from django.db import models

# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    list_display=('nombre',
     'titulo', 'pensamiento', 'telefono', 'email', 'facebook', 'likein', 'cumpleanos', 'direccion', 'github', 'curriculo', 'imagen')


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Hobbies)