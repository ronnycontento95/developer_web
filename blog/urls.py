from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
