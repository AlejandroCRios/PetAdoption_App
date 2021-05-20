from django.shortcuts import render, HttpResponse

# Create your views here.


def home (request):
    return HttpResponse("Home")

def contacto (request):
    return HttpResponse("Contacto")

def faq (request):
    return HttpResponse("Faq")
