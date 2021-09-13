from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Slider(models.Model):
    id_slider = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=50)
    imagen_base=CloudinaryField('imagen')
    subtitulo=models.CharField(max_length=50)
    url=models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
    
    def __str__(self):
        return u'%s' % self.titulo

class Customer(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.TextField(max_length=200)
    direcion=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
    
    def __str__(self):
        return u'%s' % self.titulo

class Nosotros(models.Model):
    imagen=models.ImageField(upload_to='nosotros')
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'nosotro'
        verbose_name_plural = 'nosotros'
    
    def __str__(self):
        return u'%s' % self.titulo

class Team(models.Model):
    imagen=models.ImageField(upload_to='team')
    nombre=models.CharField(max_length=50)
    cargo=models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'
    
    def __str__(self):
        return u'%s' % self.nombre
