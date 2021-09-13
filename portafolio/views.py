from portafolio.models import Portafolio
from django.shortcuts import render
from aplicacionweb.models import Slider
from portafolio.models import Portafolio
# Create your views here.
def portafolio(request):
    s=Slider.objects.all()
    portafolio=Portafolio.objects.all()
    return render(request, "portafolio/portafolio.html", {'s': s, 'portafolio': portafolio})