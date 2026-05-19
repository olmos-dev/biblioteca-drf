from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Autor
from .serializer import AutorSerializer


class AutorApiView(APIView):
  
  def get_queryset(self):
    return Autor.objects.all()
  
  #listar
  def get(self, request):
    autores = self.get_queryset()
    serializer = AutorSerializer(autores, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  
  #crear
  def post(self, request):
    autor = AutorSerializer(data = request.data)

    if autor.is_valid():
      autor.save()
      return Response(autor.data, status = status.HTTP_201_CREATED)
    
    return Response(autor.errors, status=status.HTTP_400_BAD_REQUEST)

class AutorDetailApiView(APIView):
  def get_object(self, pk):
      return get_object_or_404(Autor, pk=pk)
  
  #ver
  def get(self, request, pk):
    autor_obj = self.get_object(pk)
    serializer_autor = AutorSerializer(autor_obj)
    return Response(serializer_autor.data, status=status.HTTP_200_OK)
  
  #editar
  def put(self, request, pk):
    obj_autor = self.get_object(pk)
    autor_serializer = AutorSerializer(obj_autor,data=request.data)

    if autor_serializer.is_valid():
      autor_serializer.save()
      return Response(autor_serializer.data, status = status.HTTP_200_OK)

    return Response(autor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  #eliminar
  def delete(self, request, pk):
      obj_autor = self.get_object(pk)
      nombre = obj_autor.nombre
      obj_autor.delete()
      return Response({'message':f"Autor {nombre} se ha eliminado."}, status=status.HTTP_200_OK)


    



