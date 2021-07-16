from django import template # importando la librería de los templates.
from pages.models import Page # importando el modelo o tabla de pñáginas. con pages.models estamos haciendo referencia al modelo por fuera.


register = template.Library() # variable que hace referencia a la libreria template con el metodo Library()

# se crea el nuevo template que hará uso de esta página 
@register.simple_tag # decorador que añade esta funcionalidad, o sea que la función normal get_page_list la transformamos en un tag simple .simple_tag y la registramos @register. en la libreria de template = template.Library()
def get_page_list():
    """
    Es un template tag defiido por el desarrollador
    que su función será la de obtener la lista de páginas.
    este template tag se tiene que registrar en la librería de templates
    """
    pages = Page.objects.all() # recuperamos en Pages el objeto page o sea todas la páginas
    return pages # y las devolveremos al template en forma de template tag.
    