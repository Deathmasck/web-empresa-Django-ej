# llenado como copia del urls.py original, solo se deja el import path y el urlpaterns, y ya.
from django.urls import path
from . import views # el . indica que estamo0s haciendo referencia al mismo directorio core/ e importamos las views.py

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
]
