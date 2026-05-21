import uuid

def generar_folio():
  """ Genera un folio y lo retorna - valida que sea unico """
  from prestamos.models import Prestamo #dentro para evitar importaciones circulares
  while True:
    codigo = f'B-{uuid.uuid4().hex[:8].upper()}'
    
    folio_duplicado = Prestamo.objects.filter(folio=codigo).exists()
    
    if not folio_duplicado:
      return codigo


