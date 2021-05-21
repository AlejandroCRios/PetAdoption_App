from django.shortcuts import render, redirect
from .forms import Contact #forms.py
from django.core.mail import EmailMessage


def contacto(request):
    #importa forms que a su vez impotan models
    contact = Contact()
    
    if request.method == 'POST':
        contact = Contact(data = request.POST)
        if contact.is_valid():
            
            #reciben los datos que el usuario ingresa al formulario
            nombre = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            
            
            email = EmailMessage("Mensaje de AdoptApp", "El usuario con el nombre {} con el email {} y el telefono {}, escribre los siguiente: {} " .format(nombre,email,phone,message), 
                                 "",["newproyectosena2021@outlook.com"],reply_to=[email])

            try:
                #Envia los datos al correo del proyecto
                email.send()
                return redirect("/contacto/?valid")
            except:
                return redirect("/contacto/?invalid")
    else:
        contact = Contact()
        return render(request, 'contacto.html', {'form':contact})