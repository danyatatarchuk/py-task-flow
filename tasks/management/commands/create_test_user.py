from django.core.management.base import BaseCommand
from tasks.models import Position, Worker, TaskType


class Command(BaseCommand):
    help = "Create test user and default task types"

    def handle(self, *args, **options):
        username = "user"
        password = "user12345"

        position = Position.objects.filter(name="Developer").first()

        if not position:
            position = Position.objects.create(name="Developer")

        if not Worker.objects.filter(username=username).exists():
            Worker.objects.create_user(
                username=username,
                password=password,
                position=position,
            )
            self.stdout.write(
                self.style.SUCCESS("Test user created successfully.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Test user already exists.")
            )

        task_types = ["Bug", "Feature", "Documentation", "Testing"]

        for name in task_types:
            TaskType.objects.get_or_create(name=name)

        self.stdout.write(
            self.style.SUCCESS("Default task types created successfully.")
        )
