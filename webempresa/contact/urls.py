# llenado como copia del urls.py original, solo se deja el import path y el urlpaterns, y ya.
from django.urls import path
from . import views # el . indica que estamo0s haciendo referencia al mismo directorio core/ e importamos las views.py

urlpatterns = [
    path('', views.contact, name='contact'), # al tener en /webempresa/urls.py la configuración de la path "/contact" aquí debemos dejarla en la raíz "" esto es importante
]
