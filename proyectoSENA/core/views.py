from django.shortcuts import render, HttpResponse

# Create your views here.


def home (request):
    return render(request,"home.html")

def contacto (request):
    return render(request,"contacto.html")

def faq (request):
    return render(request,"faq.html")
