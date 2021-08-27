from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.curso, name='Curso'),
    path('total/', views.cursostotal, name='CursosTotal'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
