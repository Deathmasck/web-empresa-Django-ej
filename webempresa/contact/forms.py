#  aquí se crearán los formularios de la app contact.
from django import forms  # importando la libreria forms de django

# aquí s definen los formularios con su respectiva estructura, la cual es semejante a una tabla o modelo.
class ContactForm(forms.Form): # se crea el formulario de contact y hereda de forms.Form en lugar de models.Model 
    '''
    Es el formulario principal de Contact.
    la estructura es muy similar al definir los modelos.
    '''
    # Sus campos deben coinsidir con los del formulario frontend y serán estos:
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput( # para poder usar estilos css bootstraps sobre los campos del formulario django usamos el widget TextInput de forms  y dentro
        attrs={'class':'form-control', 'placeholder': 'Escribe tu nombre'}  # creamos el campo o diccionario attrs que guardará los atributos así esto 'class':'form-control' equivale a <input type="text" class="form-control">
    ), min_length=3, max_length=100) # otra diferencia entre los modelos es que para dar el nombre del campo en español en lugar de usar verbose_name usamos ahora "label", pues label crea dentro del html cuando se genere este formulario un tag label y dentro pone este nombre de campo 

    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput( # para poder usar estilos css bootstraps sobre los campos del formulario django usamos el widget TextInput de forms  y dentro
        attrs={'class':'form-control', 'placeholder': 'Escribe tu email'}  # creamos el campo o diccionario attrs que guardará los atributos así esto 'class':'form-control' equivale a <input type="text" class="form-control">
    ), min_length=3, max_length=100) # , required=True es un campo obligatorio, si no se llena, no se envían los datos del form.
    
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea( # aquí como ya teniamos el widget agregado widget=forms.Textarea, solo agregamos () al final  widget=forms.Textarea() y dentro agregamos el campo attrs={}
        attrs={'class':'form-control', 'rows': 3, 'placeholder': 'Escribe tu mensaje'}  # creamos el campo o diccionario attrs que guardará los atributos así esto 'class':'form-control' equivale a <textarea class="form-control"></textarea>
    ), min_length=10, max_length=1000) # en comparación a los modelos, aquí se debe usar un charfield() en lugar de un textfield para los textos grandes   -------- el widget=forms.Textarea da la apariencia de un text area al campo content que realmente es un charfield