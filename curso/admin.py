from django.contrib import admin
from .models import categoriaCurso, Curso
# Register your models here.

class CategoriaCursoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

class CursoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

admin.site.register(categoriaCurso, CategoriaCursoAdmin)
admin.site.register(Curso, CursoAdmin)
