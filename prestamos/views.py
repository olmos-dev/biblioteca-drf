from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Prestamo
from .serializer import PrestamoListarSerializer,PrestamoCreateSerializer,PrestamoDevolucionSerializer
from rest_framework import status
from django.utils import timezone
from core.utils.calcular import calcular_fecha_entrega

#Listar prestamos
class PrestamoListarApiView(APIView):
  
  def get(self, request):
    queryset = Prestamo.objects.select_related('libro','estudiante','encargado')
    serializer = PrestamoListarSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    prestamo = PrestamoCreateSerializer(data = request.data)
    
    if prestamo.is_valid():
      
      #instancia del libro
      libro = prestamo.validated_data['libro']
      
      #verificar que no este agotado
      if libro.agotado:
        return Response({"error":"Libro agotado"}, status=status.HTTP_400_BAD_REQUEST)

      #se descuenta del stock
      libro.copias_disponibles -= 1
      libro.save()

      #se agregan datos automaticos del prestamo
      prestamo.save(
        fecha_prestamo = timezone.now().date(),
        fecha_limite_entrega = calcular_fecha_entrega(timezone.now().date())
      )
      return Response(prestamo.data, status=status.HTTP_201_CREATED)
    
    return Response(prestamo.errors, status=status.HTTP_400_BAD_REQUEST)


class PrestamoDevolucionApiView(APIView):
  def patch(self, request, pk):
    try:
      prestamo = Prestamo.objects.select_related('libro').get(pk=pk)

      if prestamo.estado == 'devuelto':
        return Response({"message":"El libro ya fue devuelto"}, status=status.HTTP_400_BAD_REQUEST)
      
      libro = prestamo.libro

      #se incrementa en el stock
      libro.copias_disponibles += 1
      libro.save()

      #actualizacion automatica
      prestamo.fecha_devolucion = timezone.now().date()
      prestamo.estado = 'devuelto'
      prestamo.save()

      return Response({"message":f"Se realizo prestamos del libro: {libro.titulo} con folio: {prestamo.folio}"}, status=status.HTTP_200_OK)
    
    except Prestamo.DoesNotExist:
      return Response({"message":"Prestamo no encontrado"}, status=status.HTTP_404_NOT_FOUND)









#Acciones prestamo - ver, editar y eliminar
class PrestamoAccionesApiView(APIView):

  def get(self, request, pk):
    try:
      prestamo = Prestamo.objects.select_related('libro','estudiante','encargado').get(pk=pk)
      serializer_prestamo = PrestamoListarSerializer(prestamo)
      return Response(serializer_prestamo.data, status=status.HTTP_200_OK)
    except Prestamo.DoesNotExist:
     return Response({"message":"Prestamo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
  def put(self, request, pk):
    try:
      prestamo = Prestamo.objects.get(pk=pk)
      serializer_prestamo = PrestamoCreateUpdateSerializer(prestamo, data=request.data)
      
      if serializer_prestamo.is_valid():
        serializer_prestamo.save()
        return Response(serializer_prestamo.data, status = status.HTTP_200_OK)
      
      return Response(serializer_prestamo.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Prestamo.DoesNotExist:
     return Response({"message":"Prestamo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
  def delete(self, request, pk):
    try:
      prestamo = Prestamo.objects.get(pk=pk)
      folio = prestamo.id
      prestamo.delete()
     
      return Response({'message':f"Prestamo con folio {folio} se ha cancelado."}, status=status.HTTP_200_OK)
    
    except Prestamo.DoesNotExist:
      return Response({"message":"Prestamo no encontrado"}, status=status.HTTP_404_NOT_FOUND)


