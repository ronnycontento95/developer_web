from aplicacionweb.models import Slider
from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def perfil(request):
    print("Estoy queriendo guardar")
    sliders =Slider.objects.all()
    ctx = {'sliders': sliders}
    return render(request, 'perfil.html', ctx)
