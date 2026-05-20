from django.urls import path
from .views import PrestamoListarApiView, PrestamoAccionesApiView


urlpatterns = [
  path('prestamos/', PrestamoListarApiView.as_view(), name="listar_prestamos"),
  path('prestamo/<int:pk>/', PrestamoAccionesApiView.as_view(), name="acciones_prestamo")
]
