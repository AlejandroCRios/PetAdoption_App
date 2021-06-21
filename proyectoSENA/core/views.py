from django.shortcuts import render
from .models import Mascota,HogarPaso
from .filters import mascotaFilter
# Create your views here.

def home (request):
    
    return render(request,"home.html")




def faq (request):
    return render(request,"faq.html")



