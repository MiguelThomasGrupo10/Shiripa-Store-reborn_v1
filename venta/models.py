#   se importan random y string
import random
import string
from django.db import models
from usuarios.models import Usuarios

# Tabla Categoria y Plataforma
  
class Categoria(models.Model):
    Id_categoria     = models.BigAutoField(primary_key=True)
    categoria        = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.Id_categoria) 

class Plataforma(models.Model):
    Id_plataforma    = models.BigAutoField(primary_key=True)
    plataforma       = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Id_plataforma) 

#Modelo de la tabla VENTA
class Inventario(models.Model):
    DISPONIBILIDAD_CHOICES = (
        ('disponible', 'Disponible'),
        ('no_disponible', 'No disponible'),
    )
    
    Id_juego         = models.BigAutoField(primary_key=True)
    Id_categoria     = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Id_plataforma    = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    nombre_juego     = models.CharField(max_length=30) 
    valor            = models.DecimalField(max_digits=8, decimal_places=2)  
    stock            = models.IntegerField(default=100)  
    disponible       = models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES)

    def __str__(self):
        return str(self.nombre_juego)+" "+str(self.plataforma) 

#FUNCION LICENCIA ALEATORIA, realiza una funcion aleatoria que utiliza después la boleta
def generar_codigo_licencia():
    caracteres_permitidos = string.ascii_uppercase + string.ascii_lowercase + string.digits
    longitud_codigo = 10
    codigo_licencia = ''.join(random.choice(caracteres_permitidos) for _ in range(longitud_codigo))
    return codigo_licencia

# Obtener el nombre y valor del juego desde el Inventario hacia Boleta
def save(self, *args, **kwargs):
    inventario = Inventario.objects.get(Id_juego=self.Id_inventario_id)
    self.nombre_juego = inventario.nombre_juego
    self.valor = inventario.valor
    super().save(*args, **kwargs)    
    
# Obtener el email desde el Usuario hacia Boleta     
def save(self, *args, **kwargs):   
    usuario = Usuarios.objects.get(id_usuario=self.Id_usuario_id)
    self.email = usuario.email
    super().save(*args, **kwargs)

class Boleta(models.Model):
    Id_boleta     = models.BigAutoField(primary_key=True)
    Id_usuario    = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    nombre_juego  = models.CharField(max_length=30)
    valor         = models.DecimalField(max_digits=8, decimal_places=2)
    licencia      = models.CharField(max_length=10, default=generar_codigo_licencia) #aquí se utiliza la función
    email         = models.EmailField()

    def __str__(self):
        return str(self.Id_boleta)

    

