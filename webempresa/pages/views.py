from django.shortcuts import render, get_object_or_404  # el get_object_or_404 es un accesor de control de error 404 cuando una página no se encuentra.
from .models import Page # importamos el modelo o tabla que guarda las Page o paginas registradas coockies, aviso de priv y politica de priv.

# Create your views here.
def page(request, page_id, page_slug): # el page_id es el identificador de la página, 1, 2 o 3 correspondiente a Política de privacidad · Aviso legal · Cookies------------- El parametro page_slug es el que se definió en el path de  page/urls.py /<slug:page_slug>/ y con este parametro page_slug recuperaremos el parametro de adorno---------- Este es el Formato Slug: Una cadena, no tiene espacios ni caracteres especiales y en su lugar contiene guiones, /este-es-un-formato-slug/

    """
    una vista page para las páginas 
    """
    page = get_object_or_404(Page, id=page_id) # recuperaremos la página pasandole el modelo Page, y será filtrado por id que sería page_id
    return render(request, 'pages/sample.html', {'page':page}) # y le pasamos la página que hemos recuperado y así mostrar su titulo y contenido en el template
    