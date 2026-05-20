from django.db import models
from django.db.models import Q
from core.models import HistoricalModel


class Autor(HistoricalModel): 
  nombre = models.CharField(max_length=200)
  biografia = models.TextField(null=True, blank=True)
  fecha_nacimiento = models.DateField(null=True, blank=True)
  imagen = models.ImageField(upload_to='portadas/', null=True, blank=True)

  class Meta:
    db_table = 'autor'
    ordering = ['-id']

  def __str__(self):
        return self.nombre

class Categoria(HistoricalModel):
  nombre = models.CharField(max_length=100, unique=False)
  descripcion = models.TextField(null=True, blank=True)

  class Meta:
    db_table = 'categoria'
    ordering = ['-id']

    constraints = [
      models.UniqueConstraint(
        fields=["nombre"],
        condition=Q(deleted__isnull = True),
        name='unique_categoria_activa'
      )
    ]

  def __str__(self):
        return self.nombre

class Libro(HistoricalModel):
  autor = models.ForeignKey('Autor', related_name='libros', on_delete=models.PROTECT)
  categorias = models.ManyToManyField("Categoria", related_name="libros")
  titulo = models.CharField(max_length=255)
  isbn = models.CharField(max_length=13, unique=True)
  descripcion = models.TextField(null=True, blank=True)
  edicion = models.CharField(max_length=100, null=True, blank=True)
  editorial = models.CharField(max_length=100, null=True, blank=True)
  fecha_publicacion = models.DateField()
  no_paginas = models.PositiveIntegerField()
  
  stock = models.PositiveIntegerField(default=1)
  copias_disponibles = models.PositiveIntegerField(default=1)

  class Meta:
    db_table = 'libro'
    ordering = ['-id']

  @property
  def disponible(self):
    return self.copias_disponibles > 0
  
  @property
  def agotado(self):
    return self.copias_disponibles == 0
  
  @property
  def prestados(self):
    return self.stock - self.copias_disponibles

  def __str__(self):
        return self.titulo


