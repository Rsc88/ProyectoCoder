from django.shortcuts import render
from models import padre
from django.http import Httpresponse


# Create your views here.
def padre(self):
    Padre=padre(nombre="Alberto", apellido="suarez")
    Padre.save()
    texto=f"padre: {padre.nombre} apellido: {padre.apellido}"
    return Httpresponse(texto)

    