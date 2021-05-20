from django.shortcuts import render, redirect
from .forms import Contact #forms.py
from django.core.mail import EmailMessage

#this feature receive data from HTML and sent it through email, it isn't set for security
def contacto(request):
    contact = Contact()
    if request.method == 'POST':
        contact = Contact(data = request.POST)
        if contact.is_valid():
            nombre = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            
            
            email = EmailMessage("Message from App Django", "The user with name{} with the email {} and phone{} ,writes following: " .format(nombre,email,phone,message), 
                                 "",["             "],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valid")
            except:
                return redirect("/contacto/?invalid")
    else:
        contact = Contact()
        return render(request, 'contacto.html', {'form':contact})