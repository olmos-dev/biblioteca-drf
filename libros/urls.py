from django.urls import path
from .views import AutorApiView


urlpatterns = [
  path('autores/',AutorApiView.as_view(),name='listar_autores'),
]