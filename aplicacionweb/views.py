from aplicacionweb.models import Customer, Slider
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    sliders=Slider.objects.all()
    customers=Customer.objects.all()
    ctx={'sliders': sliders, 'customers': customers}
    return render(request, "home.html", ctx)
