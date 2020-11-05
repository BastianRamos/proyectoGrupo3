from django.contrib import admin
from .models import Empleado, Usuario, UnidadInterna

# Register your models here.
# Podemos crear una clase para modificar y agregar funcionalidades al admin.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'correo', 'telefono', 'rol', 'unidadInterna']
    search_fields = ['rut', 'nombre', 'apellido']
    list_filter = ['rol', 'unidadInterna']


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'empleado']
    search_fields = ['nombre']

class UnidadInternaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UnidadInterna, UnidadInternaAdmin)