from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """ managers para el model autor"""

    def buscar_autor(self, kword):

        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )

        return resultado
    
    def buscar_autor_ex_edad(self, kword):

        resultado = self.filter(
            nombre__icontains=kword
        ).exclude( #se puede colocar .filter para que hagga doble filtro
            Q(edad__contains=35) | Q(edad__contains=25)
        )

        return resultado
    
    def buscar_autor_edad(self, kword):

        resultado = self.filter(
            edad__gt=40,
            edad__lt=65
        ).order_by('apellidos','nombre')

        return resultado