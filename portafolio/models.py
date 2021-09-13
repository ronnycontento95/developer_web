from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Portafolio(models.Model):
    titulo=models.CharField(max_length=50)
    url=models.CharField(max_length=500)
    imagen_base=CloudinaryField('imagen')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
     

    class Meta:
        verbose_name = 'portafolio'
        verbose_name_plural = 'portafolios'
    
    def __str__(self):
        return u'%s' % self.titulo