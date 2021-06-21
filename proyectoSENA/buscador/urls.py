from django.urls import path, re_path
from .models import Mascota

from . import views


urlpatterns = [
    
    path('', views.buscador, name ='buscador'),
    path('detalleMascota/<int:idMascota>/<int:idHogarPaso>', views.detalleMascota, name='detalleMascota'),
    
]

