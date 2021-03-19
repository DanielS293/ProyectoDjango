from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Categoria, Post
from .forms import Formulario_Nuevo_Post
#def Crear_post(request):
#    return render(request, 'posts/crear-post.html')


class Nuevo_post(CreateView):
    model = 'Post'
    form_class = Formulario_Nuevo_Post
    template_name = 'posts/crear_post.html'
    success_url = reverse_lazy('home')
