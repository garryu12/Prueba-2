from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre_alumnno=models.CharField(max_length=50)
    correo_alumno=models.CharField(max_length=40)
    password_alumno=models.CharField(max_length=30)
