from rest_framework.permissions import BasePermission
from core.constants import (
    ADMINISTRADOR,
    ENCARGADO,
    ESTUDIANTE
)

#Administrador
class EsAdministrador(BasePermission):
  
  def has_permission(self, request, view):
    return (request.user.is_authenticated and request.user.groups.filter(name=ADMINISTRADOR).exists())


#Encargado
class EsEncargado(BasePermission):

  def has_permission(self, request, view):
    return (request.user.is_authenticated and request.user.groups.filter(name=ENCARGADO).exists())
  

#Estudiante
class EsEstudiante(BasePermission):
  
  def has_permission(self, request, view):
    return (request.user.is_authenticated and request.user.groups.filter(name=ESTUDIANTE).exists())