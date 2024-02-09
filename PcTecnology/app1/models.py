from django.db import models

# Create your models here.
from django.db import models
class Clientes (models.Model):
    nombre=models.CharField(max_length=30)
    email=models.CharField(max_length=50)

# Create your models here.
class Curso (models.Model):
    codigo=models.AutoField(primary_key=True)
    fecha=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)# servicios
    credito=models.CharField(max_length=50)#Importe

    def _str_(self):
        texto="{0}({1})"
        return texto.format(self.nombre,self.creditos,self.fecha)


