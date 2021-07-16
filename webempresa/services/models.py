from django.db import models

# Create your models here.
class Service(models.Model): # nombre de la tabla de services
    # atributos o campos del modelo o tabla de servicio
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services') # upload_to='services' es el directorio donde se guardarán las imágenes subidas, dir media/ aquí se creará services donde se guardarán las imagenes subidas.
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # auto_now_add=True agrega automaticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación') # auto_now_add=True agrega automaticamente la fecha de edición

    class Meta:
        verbose_name = "Servicio" # muestra nombre de la tabla en español
        verbose_name_plural = "Servicios" # muestra nombre de la tabla en plural
        ordering = ['-created'] # ordena las publicaciónes siempre de la creada más reciente hasta la más antigua

    def __str__(self): # método que devolverá el titulo del servicio.
        return self.title
    
