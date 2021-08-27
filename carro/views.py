from django.shortcuts import redirect, render
from .carro import Carro
from curso.models import Curso

# Create your views here.
def agregar_carro(request, curso_id):
    carro=Carro(request)
    curso=Curso.objects.get(id=curso_id)
    carro.agregar(curso=curso)
    return redirect('Curso')

def eliminar_carro(request, curso_id):
    carro=Carro(request)
    curso=Curso.objects.get(id=curso_id)
    carro.eliminar(curso=curso)
    return redirect('Curso')

def restar_carro(request, curso_id):
    carro=Carro(request)
    curso=Curso.objects.get(id=curso_id)
    carro.restar_curso(curso=curso)
    return redirect('Curso')

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect('Curso')