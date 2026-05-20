import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.timezone import now

from prestamos.models import Prestamo
from libros.models import Libro


class Command(BaseCommand):
    help = 'Seeder de préstamos'

    def handle(self, *args, **kwargs):

        libros = list(Libro.objects.all())
        usuarios = list(User.objects.all())

        if not libros:
            self.stdout.write(self.style.ERROR('No existen libros'))
            return

        if len(usuarios) == 0:
            self.stdout.write(
                self.style.ERROR('Debes tener usuarios')
            )
            return

        estados = ['prestado', 'devuelto', 'retrasado']

        for i in range(3):

            fecha_prestamo = now().date() - timedelta(
                days=random.randint(1, 30)
            )

            fecha_limite = fecha_prestamo + timedelta(days=7)

            estado = random.choice(estados)

            fecha_devolucion = None

            if estado == 'devuelto':
                fecha_devolucion = fecha_prestamo + timedelta(
                    days=random.randint(1, 10)
                )

            prestamo = Prestamo.objects.create(
                libro=random.choice(libros),
                estudiante=random.choice(usuarios),
                encargado=random.choice(usuarios),
                fecha_prestamo=fecha_prestamo,
                fecha_limite_entrega=fecha_limite,
                fecha_devolucion=fecha_devolucion,
                estado=estado,
                observaciones=f'Observación del préstamo {i + 1}'
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Préstamo creado: {prestamo.id}'
                )
            )

        self.stdout.write(
            self.style.SUCCESS('Seeder ejecutado correctamente')
        )