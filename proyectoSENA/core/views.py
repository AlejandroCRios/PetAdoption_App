from django.shortcuts import render
from .models import Mascota,HogarPaso

# Create your views here.

def home (request):
    
    mascota =  Mascota.objects.all()
    
    return render(request,"home.html", {"mascotas":mascota})


def faq (request):
    return render(request,"faq.html")



