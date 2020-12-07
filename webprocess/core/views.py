from django.shortcuts import render
from django.db import connection
import cx_Oracle
from core.models import *

# Create your views here. Vistas o controlador.
#Por cada vista necesitamos crear una función que nos retorna la ruta.

def inicio(request):
    return render(request, 'registration/login.html')


def tareaJefatura(request):
    data = {
        'nombre_empleados': nombre_empleados() # empleados sera la variable de acceso a la funcion creada
    }

    #PROBANDO EL PROCEDIMIENTO...
    #agregar_tarea('Realizar mantencion de ascensor', '26/12/2020', 'Ascensor A se encuentra clausurado por mal funcionamiento.', 1, 7)

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


def inicioJefatura(request):
    # Lista con todas las tareas
    tarea = Tarea.objects.all()

    # Lista de tareas en Desarrollo
    tareas_desarrollo = tarea.filter(estado = 1)

    # Lista de tareas Completadas
    tareas_completadas = tarea.filter(estado = 2)

    #Lista de tareas Atrasadas
    tareas_atrasadas = tarea.filter(estado = 3)
    return render(request, 'core/inicioJefatura.html', {'tareas':tarea, 'tareas_completadas':tareas_completadas, 'tareas_desarrollo':tareas_desarrollo, 'tareas_atrasadas':tareas_atrasadas})


def agregar_tarea(nombre, plazo, descripcion, estado_id, responsable_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('PROC_AGREGAR_TAREA', [nombre, plazo, descripcion, estado_id, responsable_id])
    return salida.getvalue()


def estado_tareas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("PROC_TOTAL_COMPLETADAS", [out_cur])
    estados = []
    for estado in out_cur:
        estados.append(estado)
    return estados


def total_completadas():
    total = Tarea.objects.get(estado=2)
    return total