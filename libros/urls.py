from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AutorApiView, AutorDetailApiView, CategoriaViewSet


router = DefaultRouter()
router.register('categorias',CategoriaViewSet,basename='categorias')

urlpatterns = [
  path('autores/',AutorApiView.as_view(),name='listar_autores'),
  path('autores/<int:pk>/', AutorDetailApiView.as_view(), name="detalle_autores"),
]

urlpatterns += router.urls

