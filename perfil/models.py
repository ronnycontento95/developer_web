from os import truncate
from django.db import models
from django.db.models.fields import CharField
from cloudinary.models import CloudinaryField


# Create your models here.
class Perfil(models.Model):
    nombre=models.CharField(max_length=100)
    titulo=models.CharField(max_length=100)
    imagen=CloudinaryField('imagen')
    pensamiento=models.TextField(max_length=500)
    telefono=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    facebook=models.CharField(max_length=50)
    likein=models.CharField(max_length=50)
    cumpleanos=models.DateField(null=True, blank=False)
    direccion=models.CharField(max_length=50)
    github=models.CharField(max_length=50)
    curriculo=models.FileField(upload_to='curriculo', null=True)
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfils'
    
    def __str__(self):
        return u'%s' % self.nombre

class Hobbies(models.Model):
    nombre=models.CharField(max_length=100)
    imagen_icono=CloudinaryField('imagen')

    class Meta:
        verbose_name = 'hobbie'
        verbose_name_plural = 'hobbies'
    
    def __str__(self):
        return u'%s' % self.nombre