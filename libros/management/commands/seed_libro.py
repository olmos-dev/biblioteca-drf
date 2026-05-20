# apps/libros/management/commands/seed_libros.py

import random
from datetime import date

from django.core.management.base import BaseCommand

from libros.models import Libro, Autor, Categoria

class Command(BaseCommand):
    help = 'Seeder de libros'


    def handle(self, *args, **kwargs):

        autores = list(Autor.objects.all())
        categorias = list(Categoria.objects.all())

        if not autores:
            self.stdout.write(
                self.style.ERROR('No existen autores')
            )
            return

        if not categorias:
            self.stdout.write(
                self.style.ERROR('No existen categorías')
            )
            return


        libros = [
            {
                "titulo": "Django for APIs",
                "descripcion": "Construcción de APIs REST con Django REST Framework.",
                "editorial": "WelcomeToCode",
                "edicion": "4ta",
                "fecha_publicacion": date(2023, 5, 10),
                "no_paginas": 320
            },
            {
                "titulo": "Two Scoops of Django",
                "descripcion": "Buenas prácticas para proyectos Django.",
                "editorial": "Two Scoops Press",
                "edicion": "3ra",
                "fecha_publicacion": date(2022, 8, 15),
                "no_paginas": 550
            },
            {
                "titulo": "Python Crash Course",
                "descripcion": "Introducción práctica a Python.",
                "editorial": "No Starch Press",
                "edicion": "2da",
                "fecha_publicacion": date(2021, 1, 20),
                "no_paginas": 544
            },
            {
                "titulo": "Fluent Python",
                "descripcion": "Programación avanzada en Python.",
                "editorial": "O'Reilly",
                "edicion": "2da",
                "fecha_publicacion": date(2022, 3, 5),
                "no_paginas": 1014
            },
            {
                "titulo": "Clean Code",
                "descripcion": "Buenas prácticas de desarrollo de software.",
                "editorial": "Prentice Hall",
                "edicion": "1ra",
                "fecha_publicacion": date(2008, 8, 1),
                "no_paginas": 464
            },
            {
                "titulo": "Designing Data-Intensive Applications",
                "descripcion": "Arquitectura y bases de datos modernas.",
                "editorial": "O'Reilly",
                "edicion": "1ra",
                "fecha_publicacion": date(2017, 3, 16),
                "no_paginas": 616
            },
            {
                "titulo": "Learning SQL",
                "descripcion": "Fundamentos de SQL y bases de datos.",
                "editorial": "O'Reilly",
                "edicion": "3ra",
                "fecha_publicacion": date(2020, 6, 10),
                "no_paginas": 394
            },
            {
                "titulo": "Django Unleashed",
                "descripcion": "Desarrollo web profesional con Django.",
                "editorial": "Pearson",
                "edicion": "1ra",
                "fecha_publicacion": date(2015, 12, 15),
                "no_paginas": 800
            },
            {
                "titulo": "REST APIs with Django",
                "descripcion": "Creación de APIs modernas con DRF.",
                "editorial": "Packt",
                "edicion": "2da",
                "fecha_publicacion": date(2024, 2, 12),
                "no_paginas": 420
            },
            {
                "titulo": "PostgreSQL Essentials",
                "descripcion": "Administración y consultas PostgreSQL.",
                "editorial": "Packt",
                "edicion": "1ra",
                "fecha_publicacion": date(2021, 7, 8),
                "no_paginas": 350
            }
        ]


        for index, libro_data in enumerate(libros, start=1):

            stock = random.randint(2, 10)
            disponibles = stock#random.randint(0, stock)

            libro, created = Libro.objects.get_or_create(
                isbn=f'9780000000{index:03}',
                defaults={
                    'autor': random.choice(autores),
                    'titulo': libro_data['titulo'],
                    'descripcion': libro_data['descripcion'],
                    'edicion': libro_data['edicion'],
                    'editorial': libro_data['editorial'],
                    'fecha_publicacion': libro_data['fecha_publicacion'],
                    'no_paginas': libro_data['no_paginas'],
                    'stock': stock,
                    'copias_disponibles': disponibles,
                }
            )

            if created:

                categorias_random = random.sample(
                    categorias,
                    k=min(1, len(categorias))
                )

                libro.categorias.set(categorias_random)

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Libro creado: {libro.titulo}'
                    )
                )

            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'El libro ya existe: {libro.titulo}'
                    )
                )


        self.stdout.write(
            self.style.SUCCESS(
                'Seeder de libros ejecutado correctamente'
            )
        )