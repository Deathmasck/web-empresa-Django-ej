"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # esto lo importamos para saber si está o no activo el debug

urlpatterns = [
    # Paths del nucleo
    path('', include('core.urls')), # url con otra configuraciñib qye proviene de urls.py de la app core.
    # Paths de app services
    path('services/', include('services.urls')), # url con otra configuraciñib qye proviene de urls.py de la app core.
    # Paths de app blog
    path('blog/', include('blog.urls')), # url con otra configuraciñib qye proviene de urls.py de la app core.
    # Paths de app pages
    path('page/', include('pages.urls')), # page/ es en singular porque mostrará de a 1en 1 las paginas 
    # Paths de app contact
    path('contact/', include('contact.urls')), # url de contact que cargará las urls de contact, dado que accederemos a contact desde aquí contact/, en las paths o urls /contact/urls.py deberiamos dejarlo desde la raíz esto es importante.
    # Paths del admin
    path('admin/', admin.site.urls),
]

# Aplicanod el truco para visualizar los ficheros media que se muestren en el navegador o panel de control admin.

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)