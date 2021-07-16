# archivo o fichero que contendrá la función que define el proceso de contexto
from .models import Link  # importando la tabla Link

def ctx_dict(request): # contexto_diccionario
    """
    creando el diccionario de contexto que se podrá usar en todos los templates de la página.
    """
    ctx = {} # ctx = contexto y es un diccionario test=hola, debe ir vacio por defecto
    links = Link.objects.all()  # buscamos todos los registros de los links en la tabla Links

    for link in links: # recorreremos cada enlace o link de red social registrado y creamos un nuevo valor al diccionario cxt = {} usando un for, o sea, llenaremos de a poco el diccionario de contexto usando el for con los datos extraidos de la variable links.
        ctx[link.key] = link.url # con los [] le indicamos que vamos a crear una clave, y esta clave la tenemos definida en el enlace link.key que sería como la asignada a twitter LINK_TWITTER  y le pasaremos de valor link.url  que url es el campo con el link de las redes sociales registradas.
    return ctx  # devuelve  el resultado del test o del di9ccionario de contexto todo lleno con sus keys y links 