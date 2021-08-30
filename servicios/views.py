from django.shortcuts import render
from servicios.models import Servicio
from aplicacionweb.models import Slider

# Create your views here.
def servicios(request):
    servicios=Servicio.objects.all()
    s = Slider.objects.all()
    ctx = {"servicios": servicios, 's': s}
    return render(request, "servicios/servicios.html", ctx)