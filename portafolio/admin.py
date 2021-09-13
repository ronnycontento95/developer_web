# Register your models here.
from django.contrib import admin 
from .models import Portafolio

# Register your models here.

class PortafolioAdmin(admin.ModelAdmin):
    exclude=('created', 'update')
    readonly_fields=('created', 'update')
    
admin.site.register(Portafolio, PortafolioAdmin)