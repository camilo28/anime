from django.db import models

# Create your models here.

class ParteDelCuerpo(models.Model):
    nombre = models.CharField(
        max_length=20,
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(ParteDelCuerpo,self).save()
    
    class Meta:
        verbose_name_plural = "Partes del cuerpo"     

class Ciudad(models.Model):
    nombre=models.CharField(
        max_length=20,
        unique=True
    ) 
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Ciudad,self).save() 
    
    class Meta:
        verbose_name_plural = "Ciudades" 

class Demonio(models.Model):
    nombre = models.CharField(
        max_length=20,
        unique=True
    )
    partedelcuerpo=models.ForeignKey(ParteDelCuerpo, on_delete=models.CASCADE,unique=True )
    def __str__(self):
        return '{}:{}'.format(self.nombre, self.partedelcuerpo.nombre)
 

    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE,unique=True)

    def __str__(self):
        return '{}:{}'.format(self.nombre, self.ciudad.nombre)
    
    class Meta:
        verbose_name_plural = "Demonios"


class Personaje(models.Model):
    nombre= models.CharField(
        max_length=20,
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Personaje,self).save()
    class Meta:
        verbose_name_plural = "Personajes"
        
class Articulo(models.Model):
    nombre=models.CharField(
        max_length=20,
        unique=True
    )
   
    personaje=models.ForeignKey(Personaje,on_delete=models.CASCADE)
    def __str__(self):
        return '{}:{}'.format(self.nombre, self.personaje.nombre)
        
    class Meta:
        verbose_name_plural = "Articulos" 

class ResultadoPelea(models.Model):
    nombre=models.CharField(
        max_length=20,
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(ResultadoPelea,self).save()
    
    class Meta:
        verbose_name_plural = "Resultados Peleas" 

class Pelea(models.Model):
    personaje=models.ForeignKey(Personaje,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.personaje.nombre)
    resultadopelea=models.ForeignKey(ResultadoPelea,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.resultadopelea.nombre)
    demonio=models.ForeignKey(Demonio,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.demonio.nombre)    
        
        