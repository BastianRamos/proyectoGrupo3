from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here. Vistas o controlador.
#Por cada vista necesitamos crear una función que nos retorna la ruta.

def inicio(request):
    return render(request, 'core/inicio.html')

def tareaJefatura(request):
    data = {
        'empleados': nombre_empleados() # empleados sera la variable de acceso a la funcion creada
    }

    # Para agregar una tarea
    if request.method == 'POST':  # POST: enviando datos
        nombre = request.POST.get('nombreTarea')
        plazo = request.POST.get('plazoTarea')
        descripcion = request.POST.get('descripcionTarea')
        estado_id = 1  # Por defecto se crea con el estado En Proceso
        responsable_id = request.POST.get('responsableTarea')
        salida = agregar_tarea(nombre, plazo, descripcion, estado_id, responsable_id)

        if salida == 1:
            data['mensaje'] = '* Tarea agregada con exito!'
        else:
            data['mensaje'] = '* ERROR: La tarea no se pudo guardar.'

    return render(request, 'core/tareaJefatura.html', data) # Con data enviamos la lista con nombres

def nombre_empleados(): # Funcion que retorna una lista con los nombres de los empleados
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # Cursor que se conecta con oracle
    out_cur = django_cursor.connection.cursor() # Cursor de salida que recibe los parametros
    cursor.callproc("PROC_NOMBRE_EMPLEADOS", [out_cur])
    nombres = []
    for nombre in out_cur:
        nombres.append(nombre) # Pasamos los elementos del cursor a una lista
    return nombres

def homeJefatura(request):
    return render(request, 'core/homeJefatura.html')

def agregar_tarea(nombre, plazo, descripcion, estado_id, responsable_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('PROC_AGREGAR_TAREA', [nombre, plazo, descripcion, estado_id, responsable_id])
    return salida.getvalue()
