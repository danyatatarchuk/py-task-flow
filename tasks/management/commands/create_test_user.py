from django.core.management.base import BaseCommand
from tasks.models import Position, Worker


class Command(BaseCommand):
    help = "Create test user"

    def handle(self, *args, **options):
        username = "user"
        password = "user12345"

        if Worker.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Test user already exists.")
            )
            return

        position = Position.objects.first()

        if not position:
            self.stdout.write(
                self.style.ERROR("No positions found.")
            )
            return

        Worker.objects.create_user(
            username=username,
            password=password,
            position=position,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Test user created with position: {position.name}"
            )
        )
