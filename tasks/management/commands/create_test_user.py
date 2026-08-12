from django.core.management.base import BaseCommand
from tasks.models import Position, Worker


class Command(BaseCommand):
    help = "Create test user"

    def handle(self, *args, **options):
        username = "user"
        password = "user12345"

        position = Position.objects.filter(name="Developer").first()

        if not position:
            position = Position.objects.create(name="Developer")

        if Worker.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Test user already exists.")
            )
            return

        Worker.objects.create_user(
            username=username,
            password=password,
            position=position,
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Test user created successfully."
            )
        )
