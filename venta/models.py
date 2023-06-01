from django.db import models

# Create your models here.
"""
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    
class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   
"""    
#Modelo de la tabla VENTA
class Inventario(models.Model):
    DISPONIBILIDAD_CHOICES = (
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
    )
    
    Id_juego         = models.BigAutoField(primary_key=True)
    categoria        = models.CharField(max_length=50)
    plataforma       = models.CharField(max_length=20)
    nombre_juego     = models.CharField(max_length=30) 
    valor            = models.DecimalField(max_digits=8, decimal_places=2)  
    stock            = models.IntegerField(default=100)  
    disponible       = models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES)

    def __str__(self):
        return str(self.nombre_juego)+" "+str(self.plataforma) 