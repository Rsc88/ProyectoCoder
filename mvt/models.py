from django.db import models
from django.db.models.lookups import LessThanOrEqual

# Create your models here.

class padre (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

class madre (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)

class abuelo(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)        

