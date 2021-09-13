from contact.forms import FormularioContacto
from aplicacionweb.models import Customer, Slider, Team
from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import EmailMessage
from perfil.models import Perfil
# Create your views here.

def home(request):
    sliders=Slider.objects.all()
    customers=Customer.objects.all()
    teams=Team.objects.all().order_by('pk')
    p=Perfil.objects.all()


    formulario_contact =FormularioContacto()
    if request.method=="POST":
        formulario_contact=FormularioContacto(data=request.POST)
        if formulario_contact.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            email=EmailMessage('Mensaje desde Django',
            'El usuario con el nombre: {} con la direccion {} escribe lo siguiente:\n\n {}'.format(nombre,email,contenido),
            "",["ronnyfer95@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contact/?valido")
            except:
                return redirect("/contact/?novalido")
    ctx={'sliders': sliders, 'customers': customers, 'teams': teams, 'miFormulario': formulario_contact, 'p': p}
    return render(request, "home.html", ctx)
