from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import CharField

class HogarPaso (models.Model):
    TIPOID = (('Cédula de ciudadanía','Cédula de ciudadanía'),
                ('NIT','NIT'),
                ('Pasaporte','Pasaporte'),
                ('Cédula de extranjería','Cédula de extranjería'),)
    
    idHogarPaso = models.BigAutoField(primary_key=True)
    nombreRazon = models.CharField("Nombre/Razon Social", max_length=50)
    tipoidentifica =models.CharField("Tipo de indentificación", max_length=50, choices= TIPOID)
    numeroidentifica = models.CharField("Numero de identificación", max_length=50)
    celular = models.CharField(max_length=30)
    direccion = models.CharField (max_length=100)
    correoE = models.CharField(max_length=50)
    
class Mascota (models.Model):
    ESPECIE = (('Perro','Perro'),
                ('Gato','Gato'),)
    
    TAMANO = (('Grande','Grande'),
                ('Mediano','Mediano'),
                ('Pequeño','Pequeño'),)
    
    GENERO = (('Macho','Macho'),
                ('Hembra','Hembra'),)
    
    VACUNACION = (('Vacunado','Vacunado'),
                ('No vacunado','No vacunado'),)
    
    ESTERILIZACION = (('Esterilizado','Esterilizado'),
                ('No esterilizado','No esterilizado'),)
    
    idMascota = models.BigAutoField(primary_key=True)
    nombreMascota = models.CharField("Nombre mascota", max_length=30)
    especieMascota = models.CharField(max_length=515, choices= ESPECIE)
    edad = models.CharField(max_length=9)
    raza = models.CharField(max_length=30)
    tamanoMascota = models.CharField("Tamaño Mascota", max_length=15, choices= TAMANO)
    genero = models.CharField(max_length=15, choices= GENERO)
    vacunacion = models.CharField(max_length=15, choices= VACUNACION)
    esterilizacion = models.CharField(max_length=30, choices=ESTERILIZACION)
    imagen = models.ImageField(upload_to ="Mascotas")
    HogarPaso = models.ForeignKey(HogarPaso, on_delete=models.CASCADE)

