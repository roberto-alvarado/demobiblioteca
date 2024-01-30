from django.db import models

# Create your models here.
class Persona(models.Model):


    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)


    class Meta:

        verbose_name = 'Persona' #Como se ve en el administrador
        verbose_name_plural = 'Personas' #Nombre del modelo en plural
        db_table = 'Persona' #Como se llamara la tabla en la db
        unique_together = ['pais','apelativo'] #Cuando se quiere que estos valores sean unique
        #reglas de integridad basicas
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]

       # abstract = True # En este caso no crea el modelo persona en la db solo lo crea para Empleado que hereda de persona y Cliente que hereda de persona

    def __str__(self):

        return self.full_name

#class Empleado(Persona):
  #  empleo = models.CharField('Empleo', max_length=50)

#class Cliente(Persona):
  #  email = models.EmailField('Email')

