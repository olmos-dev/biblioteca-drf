from rest_framework import serializers
from .models import Autor, Categoria, Libro


class AutorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Autor
    fields = ['id','nombre', 'biografia', 'fecha_nacimiento']


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id', 'nombre']


class LibroSerializer(serializers.ModelSerializer):

  disponible = serializers.ReadOnlyField()
  agotado = serializers.ReadOnlyField()
  prestados = serializers.ReadOnlyField()

  class Meta:
    model = Libro
    fields = [
      "id","autor","categorias","titulo","isbn","descripcion","edicion","editorial","fecha_publicacion","no_paginas", 
      "stock", "copias_disponibles",
      "disponible", "agotado", "prestados",
    ]
  
class LibroSimpreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Libro
    fields = ["titulo"]
    #fields = ["id","titulo"]