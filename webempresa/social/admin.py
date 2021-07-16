from django.contrib import admin
from .models import Link # Importando el mo0delo o tabla Link desde models.py en la misma carpeta /social

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # campos solo de lectura, en una tupla. para cualquier usuario...

    # configuración extendidia, para que detecte si el usaurio logueado ver si pertenece al grupo de usuario "Personal" si es así mandará a readonly_fields los campos key y name
    def get_readonly_fields(self, request, obj=None): # los 3 parametros son obligatorios, es importante request pues es quien contiene la info de tipo de grupo de usuario
        """
        una condición que verifica que el usuario logueado pertenezca al grupo de usuarios "Personal" si es muestra 4 campos de solo lectura, si no, solo 2 campos.
        """
        if request.user.groups.filter(name="Personal").exists(): # esto comprobará si dentro del grupo Personal existe el usuario, sí existe vamos a devolver el valor que tiene que sobreescribir a readonly_fields que quedaría  return la mi9sma tupla (“created”, ”updated”) pero con return (“created”, ”updated”, “key”, “name”)  
            return ('key', 'name')
        else: # si en tiempo de ejecución detectamos que el usuario que está accediendo al panel de administrador forma parte del grupo “Personal” readonly_fields pasará a tener el valor de esta tupla (“created”, ”updated”, “key”, “name”)  y si es cualquier otro tipo de usuario simplemente se harán solo lectura (“created”, ”updated”) como siempre,
            return ('updated', 'created')


admin.site.register(Link, LinkAdmin) # activando el modelo link pasandole este admin de prueba