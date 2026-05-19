from django.urls import path
from .views import AutorApiView, AutorDetailApiView


urlpatterns = [
  path('autores/',AutorApiView.as_view(),name='listar_autores'),
  path('autores/<int:pk>/', AutorDetailApiView.as_view(), name="detalle_autores"),
]