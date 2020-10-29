from django.shortcuts import render
from django.db import connection

# Create your views here. Vistas o controlador.
#Por cada vista necesitamos crear una función que nos retorna la ruta.

def inicio(request):
    return render(request, 'core/inicio.html')

def inicioJefatura(request):
    data = {
        'empleados': nombre_empleados() # empleados sera la variable de acceso a la funcion creada
    }
    return render(request, 'core/inicioJefatura.html', data) # Con data enviamos la lista con nombres

def nombre_empleados(): # Funcion que retorna una lista con los nombres de los empleados
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # Cursor que se conecta con oracle
    out_cur = django_cursor.connection.cursor() # Cursor de salida que recibe los parametros
    cursor.callproc("PROC_NOMBRE_EMPLEADOS", [out_cur])

    nombres = []

    for nombre in out_cur:
        nombres.append(nombre) # Pasamos los elementos del cursor a una lista

    return nombres