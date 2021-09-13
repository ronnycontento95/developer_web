from perfil.models import Hobbies, Perfil
from aplicacionweb.models import Slider
from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def perfil(request):
    sliders =Slider.objects.all()
    p=Perfil.objects.all()
    h= Hobbies.objects.all()
    ctx = {'sliders': sliders, 'p': p, 'h': h}
    return render(request, 'perfil.html', ctx)
