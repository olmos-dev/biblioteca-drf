from datetime import timedelta
from core.constants import DIAS_PRESTAMO


def calcular_fecha_entrega(fecha_inicio):
    dias_habiles = DIAS_PRESTAMO
    dias_agregados = 0
    fecha_actual = fecha_inicio

    while dias_agregados < dias_habiles:

        fecha_actual += timedelta(days=1)

        # 0=lunes, 6=domingo
        if fecha_actual.weekday() < 5:
            dias_agregados += 1

    return fecha_actual