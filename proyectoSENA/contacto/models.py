from django.db import models

class Contact(models.Model):
    
    
    nombre= models.CharField( max_length=200)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=200)
    mensaje = models.TextField()
    ciudad = models.CharField( max_length=30)
    
    class Meta: 
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.name