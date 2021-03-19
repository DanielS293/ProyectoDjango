from django import forms
from .models import Categoria, Post

class Formulario_Nuevo_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'categoria', 'imagen')
