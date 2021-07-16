from django.db import models
from ckeditor.fields import RichTextField # de la librería ckeditor.fields el RichTextField que sustituirá TextField del campo0 context, es nuestro editor wyziwig

# Create your models here.
class Page(models.Model): # heredará de models.Model  nota, esta clase siempre será en singular.
    # añadimos los campos de la tabla:
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Orden', default=0) # un nuevo campo de ordenación que aceptará un entero pequeño y por defecto tendrá el valor 0
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # auto_now_add=True agrega automaticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación') # auto_now_add=True agrega automaticamente la fecha de edición

    class Meta:
        verbose_name = "página" # muestra nombre de la tabla en español
        verbose_name_plural = "páginas" # muestra nombre de la tabla en plural
        ordering = ['order', 'title'] # ordenando por orden (PRIORIDAD) y después por titulo

    def __str__(self): # método que devolverá el titulo de la página.
        return self.title  # devolderá el name o nombre del título  en el panel admin.