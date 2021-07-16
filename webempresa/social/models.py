from django.db import models

# Create your models here.
class Link(models.Model): # heredará de models.Model
    # añadimos los campos de la tabla:
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True) # un campo SlugField nos obligará a usar caracteres alfanumericos guiones - o barras /, y NO nos permitirá usar espacios ni caracteres especiales, es perfecto para usarlo como   clave a modo de registro como un diccionario, o sea: (NOSOTROS VAMOS A MAPEAR ESTOS ENLACES DENTRO DE LA MEMORIA DE LA PÁGINA UTILIZANDO ESTA CLAVE O KEY Y LUEGO ACCEDEREMOS  A ELLA COMO SI FUERA UN DICCIONARIO), cláusula unique=True pues 2 redes sociales no deben tener la misma clave 
    name = models.CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True) # esto en caso de que haya varias redes sociales y el cliente no las use todas, por eso las que estén en blank=True no se mostrarán.
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # auto_now_add=True agrega automaticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación') # auto_now_add=True agrega automaticamente la fecha de edición

    class Meta:
        verbose_name = "enlace" # muestra nombre de la tabla en español
        verbose_name_plural = "enlaces" # muestra nombre de la tabla en plural
        ordering = ['name'] # ordenando por nombre

    def __str__(self): # método que devolverá el titulo del link.
        return self.name  # devolderá el name o nombre del link  en el panel admin.