from django.shortcuts import render
from .models import Service # aqui importamos del archivo models.py de /services lla cllase o modeo o tabla Service

# Create your views here.
def services(request):
    services = Service.objects.all()  # en services guardamos todos los servicios reistrados en la tablla Services con e all() obtenemos todos los servicios
    return render(request, "services/services.html", {'services': services}) # ojo, al traer desde core, tenemos que modificarle core por services pues ya no pertenecerá al core.  el diccionario de contexto se usa para traerlos a la vista o renderizar los servicios registrados