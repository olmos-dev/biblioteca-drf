from django.db import models
from django.contrib.auth.models import User
from core.models import HistoricalModel
from libros.models import Libro


class Prestamo(HistoricalModel):

  ESTADO_CHOICES = (
    ('prestado', 'Prestado'),
    ('devuelto', 'Devuelto'),
    ('retrasado', 'Retrasado'),
  )

  libro = models.ForeignKey('Libro', related_name="prestamos", on_delete=models.PROTECT)
  estudiante = models.ForeignKey('User', related_name="prestamos_estudiante", on_delete=models.PROTECT)
  encargado = models.ForeignKey('User', related_name="prestamos_registros", on_delete=models.PROTECT)
  fecha_prestamo = models.DateField()
  fecha_devolucion = models.DateField(null=True, blank=True)
  fecha_limite_entrega = models.DateField()
  estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='prestado')
  observaciones = models.TextField(null=True, blank=True)

  class Meta:
    db_table = 'prestamo'
    ordering = ['-id']
  
  def __str__(self):
    return f'{self.estudiante} - {self.libro}'


