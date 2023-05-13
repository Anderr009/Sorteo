from django.db import models

class Participante(models.Model):
    cedula = models.CharField(primary_key=True,max_length=12,db_column='cedula')
    codigo = models.CharField(unique=True,null=True,db_column='codigo',max_length=8)
    nombres = models.CharField(max_length=20,db_column='nombre')
    apellidos = models.CharField(max_length=20,db_column='apellido')
    email = models.EmailField(null=False,db_column='correo')
    telefono1 = models.CharField(max_length=25, null=False,db_column='telefono1')
    telefono1 = models.CharField(max_length=25, null=True,db_column='telefono_opcional')
    fecha_reg = models.DateField(null=True)
    
