from django.shortcuts import render # quitamos esto que solo era de pruebas, HttpResponse

''' Creando vistas:
o	Inicio home/
o	Historia about/
o	Servicios services/
o	Visítanos store/
o	Contacto contact/
o	Blog blog/
o	Sample sample/ (esta es para páginas de prueba)
'''
# Después nos llevaremos las vistas a su respectiva  app 

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")


def store(request):
    return render(request, "core/store.html")

# aquí iba la vista contact que me la lleve a /contact/views.py

# aquí iba la vista de blog que nos la llevamos a /blog/views.py

# aquí iba la vista de sampple