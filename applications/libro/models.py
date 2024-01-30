from django.db import models
from django.db.models.signals import post_save

# apps terceros
from PIL import Image

#from local apps
from applications.autor.models import Autor

from .managers import LibroManager, CategoriaManager

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', null=True, blank=True)
    visitas = models.PositiveIntegerField
    stock = models.PositiveBigIntegerField(default=0)

    objects = LibroManager()

    

    def __str__(self):
        return str(self.id) + '-' + self.titulo
    

def optimize_image(sender, instance, **kwargs):
    print(" ================== ")

    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=50, optimize=True)
            

#evento que ejecuta la señal cuando se guarda un libro
post_save.connect(optimize_image, sender=Libro)

