from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from aplicacionweb.models import Slider
from perfil.models import Perfil

def contact(request):
    s=Slider.objects.all()
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

    return render(request, "contact/contact.html",{'miFormulario': formulario_contact, 's': s, 'p':p})
    
    