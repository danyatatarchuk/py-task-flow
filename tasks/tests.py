from datetime import date

from django.test import TestCase

from tasks.models import Position, Worker, TaskType, Task


class PositionModelTest(TestCase):
    def test_position_creation(self):
        position = Position.objects.create(name="Developer")

        self.assertEqual(position.name, "Developer")
        self.assertEqual(str(position), "Developer")


class WorkerModelTest(TestCase):
    def test_worker_creation(self):
        position = Position.objects.create(name="Developer")
        worker = Worker.objects.create_user(
            username="testworker",
            password="testpass123",
            position=position,
        )

        self.assertEqual(worker.position, position)
        self.assertEqual(str(worker), "testworker")


class TaskTypeModelTest(TestCase):
    def test_task_type_creation(self):
        task_type = TaskType.objects.create(name="Bug")

        self.assertEqual(task_type.name, "Bug")
        self.assertEqual(str(task_type), "Bug")


class TaskModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker1 = Worker.objects.create_user(
            username="worker1",
            password="testpass123",
            position=self.position,
        )
        self.worker2 = Worker.objects.create_user(
            username="worker2",
            password="testpass123",
            position=self.position,
        )
        self.task_type = TaskType.objects.create(name="Bug")

    def test_task_creation(self):
        task = Task.objects.create(
            name="Fix login",
            description="Fix login issue",
            deadline=date(2026, 8, 20),
            priority=Task.Priority.HIGH,
            task_type=self.task_type,
        )

        task.assignees.add(self.worker1, self.worker2)

        self.assertEqual(task.name, "Fix login")
        self.assertEqual(task.priority, Task.Priority.HIGH)
        self.assertEqual(task.task_type, self.task_type)
        self.assertFalse(task.is_completed)
        self.assertEqual(task.assignees.count(), 2)
        self.assertIn(self.worker1, task.assignees.all())
        self.assertIn(self.worker2, task.assignees.all())
        self.assertEqual(str(task), "Fix login")
