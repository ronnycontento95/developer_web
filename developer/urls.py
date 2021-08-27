from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    url(r'^', include('aplicacionweb.urls')),
    url(r'servicios/', include('servicios.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'contact/', include('contact.urls')),
    url(r'curso/', include('curso.urls')),
    url(r'carro/', include('carro.urls')),
    url(r'perfil/', include('perfil.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
