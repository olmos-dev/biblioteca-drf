from rest_framework import serializers
from libros.serializer import LibroSimpreSerializer
from .models import Prestamo
from django.contrib.auth.models import User


class UsuarioSimpleSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["first_name", "last_name"]

class PrestamoListarSerializer(serializers.ModelSerializer):

  libro_titulo = LibroSimpreSerializer(source='libro',read_only = True)
  estudiante_nombre = UsuarioSimpleSerializer(source='estudiante',read_only = True)
  encargado_nombre = UsuarioSimpleSerializer(source='encargado',read_only = True)

  class Meta:
    model = Prestamo
    fields = ["id","folio","libro_titulo","estudiante_nombre","encargado_nombre",
              "fecha_prestamo","fecha_devolucion","fecha_limite_entrega",
              "estado","observaciones"
            ] 

class PrestamoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields = ["id","libro","estudiante","encargado", "observaciones"]

class PrestamoDevolucionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prestamo
    fields = ["fecha_devolucion","estado"]

