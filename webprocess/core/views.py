from django.shortcuts import render

# Create your views here. Vistas o controlador.
#Por cada vista necesitamos crear una función que nos retorna la ruta.

def inicio(request):
    return render(request, 'core/inicio.html')

def inicioJefatura(request):
    return render(request, 'core/inicioJefatura.html')
