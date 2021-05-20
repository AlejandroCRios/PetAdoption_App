from django.db import models

class Contact(models.Model):
    name = models.CharField("Ingresa tu nombre", max_length=200)
    email = models.EmailField("ingresa tu email",max_length=50)
    phone = models.CharField("ingresa tu numero de celular",max_length=200)
    message = models.TextField("Cuentame un poco sobre tí y porque te gustaría adoptarme!")
   
    class Meta: 
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name