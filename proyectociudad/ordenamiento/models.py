from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.


class Parroquia(models.Model):
    # Opciones de los tipos de parroquia
    # opciones_tipoParroquia = (
    #      ('rural','Parroquia Rural')
    #      ('urbana','Parroquia Urbana'))

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    # tipo = models.CharField(max_length=30, \
    #     choices=opciones_tipoParroquia)

    def __str__(self):
        return "Parroquia: Nombre: %s - Tipo: %s " % (
            self.nombre,
            self.tipo
        )


class Barrio(models.Model):
    # opciones_numParques = (
    #     ('1', 'Uno'),
    #     ('2', 'Dos'),
    #     ('3', 'Tres'),
    #     ('4', 'Cuatro'),
    #     ('5', 'Cinco'),
    #     ('6', 'Seis'),
    # )
    nombre = models.CharField(max_length=30)
    num_viviendas = models.IntegerField("num_viviendas")
    num_parques = models.IntegerField("num_parques")
    num_edificios = models.IntegerField("num_edificios")
    parroquia = models.ForeignKey(Parroquia,related_name = 'parroquias',
    on_delete= models.CASCADE)

    def __str__(self):
        return "Barrio: Nombre: %s - Numero Viviendas (%d) - Numero Parques (%d) - Numero Edificios (%d)" % ( 
            self.nombre,
            self.num_viviendas,
            self.num_parques,
            self.num_edificios)
        
