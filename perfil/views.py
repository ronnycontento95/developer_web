from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def perfil(request):
    return render(request, 'perfil.html')
