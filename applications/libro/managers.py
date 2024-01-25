import datetime

from django.db import models

from django.db.models import Q


class LibroManager(models.Manager):
    """ managers para el model libro"""

    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2024-01-01','2024-01-31' )
        )

        return resultado
    
    def listar_libros_fecha(self,kword,fecha1,fecha2):

        #convertir fechas
        date1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2,"%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1,date2)
        )

        return resultado