from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(request):
    curso=Curso.objects.all()
    return render(request,"curso/curso.html", {'cursos': curso})

def cursostotal(request):
    curso=Curso.objects.all()
    return render(request,"curso/cursostotal.html", {'cursos': curso})