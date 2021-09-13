from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.TextField(max_length=500)
    imagen=CloudinaryField('imagen')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return u'%s' % self.titulo