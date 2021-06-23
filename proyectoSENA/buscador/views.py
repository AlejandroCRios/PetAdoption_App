from django.shortcuts import render
from .models import HogarPaso, Mascota
from .filters import mascotaFilter

# Create your views here.


def buscador (request):
    
    mascota =  Mascota.objects.all()
    myfilter = mascotaFilter(request.GET, queryset= mascota)
    mascota = myfilter.qs

    
    context = {"mascotas":mascota,'filter': myfilter}
    
    return render(request,'buscador.html', context)

def detalleMascota (request, idMascota, idHogarPaso):
    
    mascota = Mascota.objects.get(idMascota=idMascota)
    hogar = HogarPaso.objects.get(idHogarPaso=idHogarPaso)
    
    
    context = {"mascota":mascota, "hogar": hogar}
    
    return render(request,'detalleMascota.html', context)