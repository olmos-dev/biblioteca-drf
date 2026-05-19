from django.core.management.base import BaseCommand

from faker import Faker

from libros.models import Autor

fake = Faker()

class Command(BaseCommand):

    help = 'Seeder de autores'

    def handle(self, *args, **kwargs):
        
        for _ in range(5):
            
            Autor.objects.create(
                nombre=fake.name(),
                biografia=fake.text(),
                fecha_nacimiento=fake.date()
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Autores creados correctamente'
            )
        )