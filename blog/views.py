from django.shortcuts import render, HttpResponse
#importmos la classe del modelo
from blog.models import Categoria, Post
from aplicacionweb.models import Slider

# Create your views here.
#blog/blog.html busca dentro de la carpeta blog la subcarpeta blog.html

def blog(request):
    posts=Post.objects.all()
    s=Slider.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, 's': s})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html",{'categoria': categoria, 'posts': posts})