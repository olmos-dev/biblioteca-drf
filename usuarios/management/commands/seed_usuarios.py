from django.core.management.base import BaseCommand

from django.contrib.auth.models import (
    User,
    Group
)

from core.constants import (
    ADMINISTRADOR,
    ENCARGADO,
    ESTUDIANTE
)


class Command(BaseCommand):

    help = 'Seeder de usuarios y grupos'

    def handle(self, *args, **kwargs):
        #crear grupos
        grupo_admin, _ = Group.objects.get_or_create(name=ADMINISTRADOR)
        grupo_encargado, _ = Group.objects.get_or_create(name=ENCARGADO)
        grupo_estudiante, _ = Group.objects.get_or_create(name=ESTUDIANTE)

        #crear usuarios
        usuarios = [
            {
                "username": "Alberto",
                "password": "123",
                "email":"alberto@mail.com",
                "group": grupo_admin
            },

            {
                "username": "Ana",
                "email":"ana@mail.com",
                "password": "123",
                "group": grupo_encargado
            },

            {
                "username": "Jose",
                "email":"jose@mail.com",
                "password": "123",
                "group": grupo_estudiante
            },
        ]


        for user_data in usuarios:
            usuario, creado = User.objects.get_or_create(
                username=user_data["username"],
                email = user_data["email"]
            )

            if creado:
                usuario.set_password(
                    user_data["password"]
                )
                usuario.save()
                usuario.groups.add(
                    user_data["group"]
                )
                usuario.is_staff = True
                usuario.is_superuser = True
                usuario.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Usuario creado: {usuario.username}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Usuario ya existe: {usuario.username}'
                    )
                )

        self.stdout.write(

            self.style.SUCCESS(
                'Seeder ejecutado correctamente'
            )
        )