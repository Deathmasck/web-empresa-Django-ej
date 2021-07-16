from django.shortcuts import render, redirect # función redirec sirve para redireccionar páginas.
from django.urls import reverse # función que funciona como el template tag url
from .forms import ContactForm # importamos el formulario ContactForm desde forms.py en el mismo directorio /contact/
from django.core.mail import EmailMessage #  Sirve para crear la estructura de un mensaje e Incluye un método para enviarlo 

# Create your views here.
def contact(request):
    #print("Tipo de petición:::: {}".format(request.method)) # con esto imprimimos en consola el tipo de petición antes y después de enviar datos al formulario. Nos indica el método con el que se ha hecho la petición a la página.
    contact_form = ContactForm() # Instanciando el formulario antes de enviarlo al contact.html
    
    if request.method == "POST": # para comprobar que el método de la petición sea igual a POST
        contact_form = ContactForm(data=request.POST) # CON ESTO RELLENAREMOS LA PLANTILLA con los campos previamente enviados, de forma automatica.
        if contact_form.is_valid(): # comprueba si todos los campos han si9do llenados correctamente y si es así, manda True
            name = request.POST.get('name', '') # recuperando los datos enviados por el formulario, en caso de que se hayan enviado de forma correcta, name = nombre del campo nombre, recibimos la petición POST con request.POST y usamos el accesor .get para obtener el vampor que hay en la clave name ('name') y si no hay ninguno que nos devuelva una cadena vacía (, '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviando el correo y redireccionando
            email = EmailMessage( # función EmailMenssage que contendrá la estructura para enviar por correo al webmaster de lla página 
                "La Caffetiera: Nuevo mensaje de contacto", # asunto,El asunto un campo de texto que diga la cafetería nuevo mensaje de contacto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), # cuerpo,   entre {} {} {}van tomando el lugar del format respectivamente,  Para el cuerpo tenemos que crear una estructura Que nos permita Mostrar la información de la persona Que nos quiere contactar su correo y el contenido 
                "no-contestar@mailbox.emailtrap.io", # email_origel, En el email de Origen Con esto damos a entender que si quieren contestar este mensaje pues nadie le va a responder Aquí se puede poner un correo de la empresa que concuerde con El dominio que se tiene registrado Ya que proveedores como Gmail comprueban si concuerdan Los emails Con el servidor desde donde se está enviando el correo Y si no concuerdan los meterá directo al spam Por eso hay que tener mucho cuidado con esto 
                ["deathmasck@devinge.net"], # email_destiono, En el email se destino tenemos que poner una lista Con todos los emails dónde queremos enviar este mensaje Aquí podríamos poner diferentes Correos en las personas que se encargan de verificar todos los emails que llegan de contacto para que los atiendan 
                reply_to=[email] # Qué es el correo donde va a responder la persona que recibió este correo, qué es el de la persona que se pone en contacto Para que automáticamente nosotros nos ponemos en contacto con ella para responderle Su mensaje, En el reply_to ya tenemos el campo email y ya hemos puesto antes
            )

            try: # capturando el posible error.
                email.send() # con esto se envía el correo al webmaster o quien atenderá los correos de contacto.
                # Todo ha ido bien, entonces redireccionará a OK
                return redirect(reverse('contact')+'?ok') # redirección dinamica que funcio0na como un Tt url 
            except: # cuando falla entra aquí...
                # algo no ha ido bien, entonces redireccionamos a FAIL.
                return redirect(reverse('contact')+'?fail') # redirección dinamica que funcio0na como un Tt url, para que muestre un error en el template debemos editar en el template cuando recibimos la variable pore get "fail"

            
    
    return render(request, "contact/contact.html", {'form':contact_form}) # al pasar el template de /core/templates/core/contact.html a /contact/templates/contact/contact.html, cambiamos "core/contact.html" por "contact/contact.html"