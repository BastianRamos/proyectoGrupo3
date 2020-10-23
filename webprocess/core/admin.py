from django.contrib import admin
from .models import Empleado, Usuario

# Register your models here.
# Podemos crear una clase para modificar y agregar funcionalidades al admin.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','correo','telefono','rol']
    search_fields = ['rut','nombre','apellido']
    list_filter = ['rol']


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Usuario, UsuarioAdmin)