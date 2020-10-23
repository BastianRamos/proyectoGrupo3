from django.urls import path
from .views import inicio, inicioJefatura

#Para agregar una nueva vista se debe importar desde Views y luego agregar el path al urlpatterns.

urlpatterns = [
    #path('ruta del navegador', funcion creada en views y asignamos un nombre.)
    path('', inicio, name="inicio"),
    path('inicioJefatura/', inicioJefatura, name="inicioJefatura")
]