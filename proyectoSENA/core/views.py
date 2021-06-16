from django.shortcuts import render
from .models import Mascota,HogarPaso
from .filters import mascotaFilter
# Create your views here.

def home (request):
    
    mascota =  Mascota.objects.all()
    myfilter = mascotaFilter(request.GET, queryset= mascota)
    mascota = myfilter.qs
    context = {"mascotas":mascota,'filter': myfilter}
    
    return render(request,"home.html", context)

def buscador (request):
    
    mascota =  Mascota.objects.all()
    myfilter = mascotaFilter(request.GET, queryset= mascota)
    mascota = myfilter.qs
    context = {"mascotas":mascota,'filter': myfilter}
    
    return render(request,"buscador.html", context)


def faq (request):
    return render(request,"faq.html")



