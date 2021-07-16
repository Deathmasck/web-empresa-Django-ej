from django.shortcuts import render, get_object_or_404 # accesor  get_object_or_404  
from .models import Post, Category # cargando el modelo Post y la tabla Category 

# Create your views here.
def blog(request): # vista que nos trajimos desde /core/views.py
    posts = Post.objects.all()  # con objects.all() recuperaremos todos los mensajes y los pasaremos a la variable post.
    return render(request, "blog/blog.html", {'posts':posts})  # , {'posts':posts} es un diccionario de contexto, este diccionario con posts se pasa directo al template blog.html por este return.

def category(request, category_id): # category_id será el identificador único de cada registro de categoria.
    """
    Es la vista que recivirá en category_id el identificador de categoria o id o pk 
    """
    category = get_object_or_404(Category, id=category_id) # el .get nos permite RECOGER UN UNICO registro filtrado por una serie de campos, pero en nuestro caso será el id = category_id y esto buscará el id de la categoria y lo guardará en la variable.  Para control de error 404 cambiamos a la función get_object_or_404 con los campos (Category, id=category_id) 

    #posts = Post.objects.filter(categories=category)  comentada porque no pasaremos post para aplicar el otro método... # todos los post o publicaciones serán filtrados .filter por categorieas, categories=category  y se mostrarán lo que coinsidan con el id que contenga  la variable  category. 

    #return render(request, 'blog/category.html', {'category':category, 'posts':posts}) comentado para aplicar el o0tro metodo, borramos el diccionario de contexto posts: #  y finalmente le pasaremos el diccionario de contexto {'posts':posts} para que finalmente nos muestre los post publicados con esa categoria filtrada category. {'posts':posts}
    return render(request, 'blog/category.html', {'category':category})