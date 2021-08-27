from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.contact, name='Contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
