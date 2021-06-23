
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
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            phone = request.POST.get("telefono")
            city = request.POST.get("ciudad")
            message = request.POST.get("mensaje")
            
                                                                                             
            email = EmailMessage("Mensaje enviado desde PetAdoption por {}".format(nombre), "========================================================= Nombre del remitente: {} ========================================================= Email del remitente: {} ========================================================= Teléfono: {} ========================================================= Ciudad: {}  ========================================================= Contenido del mensaje: {} " .format(nombre,email,phone,city,message), 
                                 "",["newproyectosena2021@outlook.com"],reply_to=[email])

            try:
                #Envia los datos al correo del proyecto
                email.send()
                return redirect("home")
            except:
                return redirect("contacto")
    else:
        contact = Contact()
        return render(request, 'contacto.html', {'form':contact})

