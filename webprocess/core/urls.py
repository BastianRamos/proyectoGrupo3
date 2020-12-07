from django.urls import path, include
from .views import inicio, tareaJefatura, inicioJefatura

#Para agregar una nueva vista se debe importar desde Views y luego agregar el path al urlpatterns.

urlpatterns = [
    #path('ruta del navegador', funcion creada en views y asignamos un nombre.)
    path('', inicio, name="inicio"),
    path('tareaJefatura/', tareaJefatura, name="tareaJefatura"),
    path('inicioJefatura/', inicioJefatura, name="inicioJefatura"),
    path('accounts/', include('django.contrib.auth.urls')),# Gestion de cuentas de Django para login, logout y otros...
]