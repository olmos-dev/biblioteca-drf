from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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



