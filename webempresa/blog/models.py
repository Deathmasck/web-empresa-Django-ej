from django.db import models
from django.contrib.auth.models import User # User, es el modelo de usuarios que contiene todos los usuarios que están registrados en el panel de administador 
from django.utils.timezone import now # libreria importada que detecta la zona horaria en donde está configurado el proyecto 
from ckeditor.fields import RichTextField # de la librería ckeditor.fields el RichTextField que sustituirá TextField del campo0 context, es nuestro editor wyziwig

# Create your models here.
class Category(models.Model):
    """
    modelo o tabla que guardará las categorias a las que 
    pertenece cada post o entrada o publicación dentro del blog
    """
    name = models.CharField(max_length=140, verbose_name='Nombre')  # nombre del titulo  de la categoria

    # las columnas created y updated y  Meta yy __str__ se reusaron desde models.py de services app. 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # auto_now_add=True agrega automaticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación') # auto_now_add=True agrega automaticamente la fecha de edición

    class Meta:
        verbose_name = "categoria" # muestra nombre de la tabla en español
        verbose_name_plural = "categorias" # muestra nombre de la tabla en plural
        ordering = ['-created'] # ordena las publicaciónes siempre de la creada más reciente hasta la más antigua

    def __str__(self): # método que devolverá el titulo de la categoria.
        return self.name  # devolderá el name o nombre de categoria.
    
class Post(models.Model):
    """
    Es la tabla que guardará las pubicacionmes entradas o post del blog
    """
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now) # se recomienda usar defautlt=timezone.now() pa obtener  la hora actual usando la librería timezone django importada from django.utils import timezone, debría ser solo default=now immportando así: from django.utils.timezone import now
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True) # las imagenes se guardarán en media/blog y los null y blank en True son para que el usuario no se vea obliigado a introducir una imagen en su publicació, si no la suben no marca error.

    # campos con relaciones de claves foraneas o muchos a muchos
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE) # foreignkey es el tipo de dato del campo, User es el nombre de usuario que está registrado en los usuarios de django que podrán registrar entradas, o sea, User es la clave foranea importada arriba,  y on_delete= models.CASCADE, con eso se borrarán toooodas las publicaciones echas por un usuario que ha sido eliminado, pero si usamos on_delete=models.PROTECT TEENEMOS  que aompañarlo de estos parametros null=True, blank=True para que django permita dejar en blanco este campo. y no se borrarán las publicaciones hechar por el usuario eliminado de Users.
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_post') # campo que guardará las categorias a las que pertenece la publicación hecha del blog, campo ManyToMany  o sea, 1 entrada puede tener muchas categorias.  /// related_name='get_post' es utilizado para renombrar una referencia y renombrarla de forma más lógica.
    
    # las columnas created y updated y  Meta yy __str__ se reusaron desde models.py de services app. 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') # auto_now_add=True agrega automaticamente la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación') # auto_now_add=True agrega automaticamente la fecha de edición

    class Meta:
        verbose_name = "entrada" # muestra nombre de la tabla en español
        verbose_name_plural = "entradas" # muestra nombre de la tabla en plural
        ordering = ['-created'] # ordena las publicaciónes siempre de la creada más reciente hasta la más antigua

    def __str__(self): # método que devolverá el titulo de la categoria.
        return self.title  # devolderá el name o nombre de categoria.