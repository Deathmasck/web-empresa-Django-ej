from django.contrib import admin
from .models import Service # con esto importamos el modelo o tabla Service que está en el archivo models.py de este mismo directorio /services/

# Register your models here.
class ServiceAdmin(admin.ModelAdmin): # config básica del admin.
    readonly_fields = ('created', 'updated') # campos que serán de solo lectura

admin.site.register(Service, ServiceAdmin) # Registrando el servicio Service y su configuración ServiceAdmin
