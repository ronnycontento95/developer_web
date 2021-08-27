from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

admin.site.register(Categoria, PostAdmin)
admin.site.register(Post, PostAdmin)

