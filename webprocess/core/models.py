from django.db import models

# Create your models here.
#Declaramos una clase por cada tabla de nuestro modelo de datos.
#Django genera una ID automatica y autoincrementable para cada tabla.
#python manage.py makemigrtions <--- Lee el archivo models y crea una migración.
#python manage.py migrate <--- Toma las migraciones pendientes y las enlaza con la base de datos.
#python manage.py createsuperuser <--- Creamos un super usuario para la administración del sitio con Django.

class Empleado(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    rol = models.CharField(max_length=40)

    def __str__(self):
        string = self.nombre + " " + self.apellido
        return string

class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    password = models.CharField(max_length=10, verbose_name="Contraseña")
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre