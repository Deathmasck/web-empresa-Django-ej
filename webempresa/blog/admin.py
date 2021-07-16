from django.contrib import admin
from .models import Category, Post # importando las tablas o modelos creados dentro de /blog/models.py

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """
    modelo category registrado
    """
    readonly_fields = ('created', 'updated') # son los campos de solo lectura.

class PostAdmin(admin.ModelAdmin):
    """
    modelo post registrado
    """
    readonly_fields = ('created', 'updated') # son los campos de solo lectura.
    # otros campos para personalizar el panel admin:
    list_display = ('title', 'author', 'published', 'post_categories',) # que recibirá una tupla, en donde se le indican las columnas que se desean mostrar en el panel admin de post,  el 'post_categories', es la columna que nosotros creamos como método.
    ordering = ('author', 'published') # le pasamos en la tupla los campos que deseamos ordenara, podemos agregar un orden de ordenación, primero se ordenará por author y después por el subcampo published, o sea, primero se ordenarán por autor y después por fecha de publicación. Y si deseamos ordenar por 1 solo campo tenemos que dejar la tupla así ('author',)  con la , para indicarle que es una tupla, de lo contrario marcará error

    search_fields = ('title', 'content', 'author__username', 'categories__name') # se crea un campo de búsqueda en el panel admin para buscar por título, podemos buscar también por "contenido" cae destacar que buscará cualquier palabra o letra que coinsida en el contenido de la entrada, si deseamos buscar por autor registtrado en django debemos usar una sintaxis especial author__username con el __ hacemos referencia a que buscará en el campo que tiene el modelo de usuario registrados, y finalmente también podemos buscar pr el campo ManyToMany de categorias igual usando la sintaxis especial categories__name name hace referencia al nombre de la categoria en la relación muchos a muchos del modelo de blog. 

    date_hierarchy = 'published' # nos filtrará las fechas de publicación por dias, mes y años, o todos los años, esto abajo del campo de busqueda.
    list_filter  = ('author__username', 'categories__name',) # se agregará una sección de filtrado por autor, para que muestre todos los autores que hay registrados y al dar clic sobre alguno nos dará sus entradas realizadas. Recordar que author lleva __username porque tiene una relación foreign key con los usuarios registrados y que categoria lleva category__name o nombre de categoria que es una relación de muchos a muchos dentro del models.py de blog.


    def post_categories(self, obj): # obj = hará referencia a cada fila, elemento, instancia o registro que se estará mostrando en la lista, se recorrerá para cada fila, o sea, se ejecutará el código para cada instancia o registro.
        """
        post_categories hace referencia a las categorias que tiene la entrada o publicación y queremos listar en una nueva columna que no puede mostrarse por medio de list_display = ('',)
        """
                # el join nos junta en forma de lista
                          # sacando el nombre "cat.name" para "for" categoria "cat" en "in" el objeto categorias "obj.categories" <-- accediendo al campo manytomany, a buscar todas las categorias "all()" y ordenarlas por nombre "order_by('name')"
        return ", ".join([cat.name for cat in obj.categories.all().order_by("name")]) # o sea, esto generará una cadena de caracteres con los nombres de todas las categorias separadas por comas

    # sustituimos el nombre post_categories por Categorias para mostrarse en columna
    post_categories.short_description = "Categorias"  # usando el atributo de short_description para sustituir el nombre de columna  post_categories por Categorias.

# registrando cambios en el administrador y entonces se mostrarán en el admin panelñl
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)