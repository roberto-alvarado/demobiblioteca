from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView

# models local
from .models import Autor
# Create your views here.


class ListAutores(ListView):
    model = Autor
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')

        return Autor.objects.buscar_autor(palabra_clave)