from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='buba@lupa.cam',
            first_name='Buba',
            last_name='LupaCum',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Buba2402')
        user.save()