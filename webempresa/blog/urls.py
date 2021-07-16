# llenado como copia del urls.py original, solo se deja el import path y el urlpaterns, y ya.
from django.urls import path
from . import views # el . indica que estamo0s haciendo referencia al mismo directorio blog/ e importamos las views.py

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
    # para entra a ver una categoria, es importante cerrar con la barra "/", la views.category  es la vista recién creada, y el nombre que tendrá la vista name será category
                # <ctaegory_id> es un campo dinamico, se detectará lo que haya entre las barras / <> /  y lo tomará como parametro que pasará a la vista en el parametro category_id del    def category(request, category_id):
                # estos parametros dinámicos <ctaegory_id> por defecto siempre será pasado como una cadena de caracteres,  o sea, son detectados en el path, siempre  como cadena de caracteres, 
                    # pero puesto que el id o pk que Queremos pasar comoo parametro es un entero tenemos que forzar a convertir la cadena <ctaegory_id> a un entero con solo colocarle int: antes de category_id  lo cual cambiará la string por un entero y lo enviará al parametro de la vista con el cual p0odremos usar para filtrar en la consulta las entradas que tenga esa categoria    https://docs.djangoproject.com/en/2.0/topics/http/urls/#path-converters documentación sobre los conversores de tipo en el path
]
