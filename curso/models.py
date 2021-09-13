from django.db import models
from django.db.models.base import Model
from cloudinary.models import CloudinaryField

# Create your models here.
class categoriaCurso(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriacurso'
        verbose_name_plural = 'categoriacursos'

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(categoriaCurso, on_delete=models.CASCADE)
    imagen=CloudinaryField('imagen')
    precio=models.FloatField()
    disponivilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        
    def __str__(self):
        return self.nombre