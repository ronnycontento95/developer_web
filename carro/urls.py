from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='carro'
urlpatterns = [
    path('agregar/<int:curso_id>/', views.agregar_carro, name='agregar'),
    path('eliminar/<int:curso_id>/', views.eliminar_carro, name='eliminar'),
    path('restar/<int:curso_id>/', views.restar_carro, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
