from django.db import models

# Create your models here.
#======proveedor

lista_producto= [
    [0,"llantas"],
    [1,"aceite"],
    [2,"baterias"],
    [3,"encera pintura"]
]

class MarcaPro(models.Model):
    productos = models.IntegerField(choices=lista_producto)
        

class Proveedor(models.Model):
    telefono = models.CharField(max_length=(50))
    correo = models.EmailField()
    direccion = models.CharField(max_length=(50))
    nombre_emp = models.CharField(max_length=(50))
    productos = models.ForeignKey(MarcaPro, on_delete=models.PROTECT)
        
    def _str_(self):
        return self.nombre

#======Material
class MarcaMat(models.Model):
    nombre = models.CharField(max_length=(50))
        
    def _str_(self):
        return self.nombre
    
class Material(models.Model):
    nombre = models.CharField(max_length=(50))
    modelo = models.CharField(max_length=(50))
    marca = models.ForeignKey(MarcaMat, on_delete=models.PROTECT)
    caracteristica = models.TextField()
    fechaVen= models.DateField()
    precio= models.IntegerField()
    

    def _str_(self):
        return self.nombre

#======Herramientas

class MarcaHer(models.Model):
    nombre = models.CharField(max_length=(50))
        
    def _str_(self):
        return self.nombre
    
class herramientas(models.Model):
    nombre = models.CharField(max_length=(50))
    modelo = models.CharField(max_length=(50))
    marca = models.ForeignKey(MarcaHer, on_delete=models.PROTECT)
    caracteristica = models.TextField()
    coste= models.IntegerField()
    fechaVen= models.DateField()
    manual= models.BooleanField()

    def _str_(self):
        return self.nombre

#======Maquinaria
class MarcaMac(models.Model):
    nombre = models.CharField(max_length=(50))
        
    def _str_(self):
        return self.nombre

class Maquinaria(models.Model):
    nombre = models.CharField(max_length=(50))
    modelo = models.CharField(max_length=(50))
    marca = models.ForeignKey(MarcaMac, on_delete=models.PROTECT)
    caracteristica = models.TextField()
    certificacion = models.BooleanField()
    coste= models.IntegerField()
    manual= models.BooleanField()

    def _str_(self):
        return self.nombre

#========agendar servisio
class Marca(models.Model):
    nombre = models.CharField(max_length=(50))
        
    def _str_(self):
        return self.nombre
    
opciones_servicio =[
    [0,"revision general"],
    [1,"revision componetes"],
    [2,"revision electronica"],
    [3,"cambio de liquidos"],
    [4,"cambio/recarga bateria"],
    [5,"bulca"],
    [6,"aboyaduras"],
    [7,"otros servicios"]
]



class Cita(models.Model):
    nombre = models.CharField(max_length=(60))
    email = models.EmailField()
    modelo = models.CharField(max_length=(150))
    patente = models.CharField(max_length=(10))
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    servicio = models.IntegerField(choices=opciones_servicio)
    fecha = models.DateField()
    precio = models.IntegerField()
    

    def _str_(self):
        return self.patente

#=========para formulario de contacto
opciones_comentarios = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=(60))
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_comentarios)
    mensage = models.TextField()
    avisos = models.BooleanField()

    def _str_(self):
        return self.nombre