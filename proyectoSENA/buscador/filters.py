
import django_filters

from .models import *


class  mascotaFilter (django_filters.FilterSet):
    class Meta:
        model = Mascota 
        fields = ['especieMascota', 'tamanoMascota', 'sexo', 'HogarPaso__ciudad']
        