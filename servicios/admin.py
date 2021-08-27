from django.contrib import admin 
from .models import Servicio

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    exclude=('created', 'update')
    readonly_fields=('created', 'update')
    
admin.site.register(Servicio, ServiciosAdmin)