from django.contrib import admin
from .models import Customer, Nosotros, Slider, Team

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display=(
        'imagen_base',
        'titulo',
        'subtitulo',
    )

class CustomerAdmin(admin.ModelAdmin):
    list_display=(
        'titulo',
        'subtitulo',
        'direcion',
    )

class NosotrosAdmin(admin.ModelAdmin):
    list_display=(
        'imagen',
        'titulo',
        'subtitulo',
    )

class TeamAdmin(admin.ModelAdmin):
    list_display=(
        'imagen',
        'nombre',
        'cargo',
    )

admin.site.register(Slider, SliderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Team, TeamAdmin)
