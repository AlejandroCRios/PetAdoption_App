from django.db.models import fields
import django_filters
from django_filters import filters
from .models import *
from django_filters import ChoiceFilter

class  mascotaFilter (django_filters.FilterSet):
    class Meta:
        model = Mascota 
        fields = ['especieMascota', 'tamanoMascota', 'sexo', 'HogarPaso__ciudad']
        