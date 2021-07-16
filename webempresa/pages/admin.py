from django.contrib import admin
from .models import Page # Importando el mo0delo o tabla Page desde models.py en la misma carpeta /pages

# Register your models here.
class PageAdmin(admin.ModelAdmin): # solo agregamos Page
    readonly_fields = ('created', 'updated') # campos solo de lectura, en una tupla.
    list_display = ('title', 'order') # para que se muestre la columna para ordenar los registros. que es una tupla de nombres de campos para que se muestre como columnas en la página de lista de cambios para el objeto, en el panel admin GESTOR DE PÁGINAS, se mostrará primero la columna titulo y después el orden.

admin.site.register(Page, PageAdmin) # activando el modelo Page en el panel admin