from django.db import models

# Create your models here.
#Declaramos una clase por cada tabla de nuestro modelo de datos.
#Django genera una ID automatica y autoincrementable para cada tabla.
#python manage.py makemigrations <--- Lee el archivo models y crea una migración.
#python manage.py migrate <--- Toma las migraciones pendientes y las enlaza con la base de datos.
#python manage.py createsuperuser <--- Creamos un super usuario para la administración del sitio con Django.


class UnidadInterna(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


# LIST PARA ROL DE EMPLEADO
rol_funcionarios = [ # Creamos una lista para almacenar en tuplas las opciones de ROL de la tabla Empleado
    (1, 'Funcionario Gerente'), # Accedemos al elemento a traves del index
    (2, 'Funcionario Jefe'),
    (3, 'Funcionario Subordinado'),
    (4, 'Diseñador de Procesos')
]


class Empleado(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    rol = models.IntegerField( # Se visualiza como un Select en Django
        null=False, blank=False,
        choices=rol_funcionarios # Indicamos que las opciones del Select estan en la lista rol_funcionarios
    )
    unidadInterna = models.ForeignKey(UnidadInterna, on_delete=models.PROTECT, verbose_name='Unidad Interna')

    def __str__(self):
        string = self.nombre + " " + self.apellido
        return string


class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    password = models.CharField(max_length=10, verbose_name="Contraseña") # En Django se visualizara como Contraseña en vez de password
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


# LIST PARA ESTADO DE TAREA
estado_tarea = [
    (1, 'En Desarrollo'),
    (2, 'Completada'),
    (3, 'Atrasada')
]


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    plazo = models.DateField()
    descripcion = models.CharField(max_length=300)
    estado = models.IntegerField(
        null=False, blank=False,
        choices=estado_tarea
    )
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class FlujoTarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    responsable = models.ForeignKey(Empleado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Notificacion(models.Model):
    asunto = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateField()

    def __str__(self):
        return self.asunto