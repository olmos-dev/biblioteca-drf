from django.core.management.base import BaseCommand

from faker import Faker

from libros.models import Categoria

fake = Faker()

class Command(BaseCommand):

    help = 'Seeder de categorias'

    def handle(self, *args, **kwargs):
        
        categorias = [
          {"nombre":"Programación", "descripcion":None},
          {"nombre":"Ingenieria de software","descripcion":None},
          {"nombre":"Base de datos","descripcion":None},
          {"nombre":"Inteligencia Artificial","descripcion":None},
          {"nombre":"Administracion de proyectos","descripcion":None},
          {"nombre":"Desarrollo Backend","descripcion":None},
          {"nombre":"Desarrollo Frontend","descripcion":None},
          {"nombre":"API RESTful","descripcion":None},
          {"nombre":"Python","descripcion":None},
        ]
        
        for cat in categorias:
            objeto, creado = Categoria.objects.update_or_create(
                nombre=cat["nombre"],
                defaults={"descripcion": cat["descripcion"]}
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Categorias creadas correctamente'
            )
        )