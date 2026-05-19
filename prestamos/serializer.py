from rest_framework import serializers
from libros.serializer import LibroSimpreSerializer
from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
  
  libro = LibroSimpreSerializer(read_only = True)
  
  class Meta:
    model = Prestamo
    fields = ["id","libro","estudiante","encargo",
              "fecha_prestamo","fecha_devolucion","fecha_limite_entrega",
              "estado","observaciones"
            ] 