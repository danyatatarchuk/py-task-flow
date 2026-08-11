from datetime import date

from django.test import TestCase
from django.urls import reverse

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


class WorkerViewsTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testworker",
            password="testpass123",
            position=self.position,
        )

    def test_worker_list_view(self):
        response = self.client.get(reverse("worker-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/worker_list.html")
        self.assertContains(response, "testworker")

    def test_worker_detail_view(self):
        response = self.client.get(
            reverse("worker-detail", args=[self.worker.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/worker_detail.html")
        self.assertContains(response, "testworker")
        self.assertContains(response, "Developer")


class TaskViewsTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testworker",
            password="testpass123",
            position=self.position,
        )
        self.task_type = TaskType.objects.create(name="Bug")

        self.task = Task.objects.create(
            name="Fix login",
            description="Fix login issue",
            deadline=date(2026, 8, 20),
            priority=Task.Priority.HIGH,
            task_type=self.task_type,
        )

        self.task.assignees.add(self.worker)

    def test_task_list_view(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_list.html")
        self.assertContains(response, "Fix login")

    def test_task_detail_view(self):
        response = self.client.get(
            reverse("task-detail", args=[self.task.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_detail.html")
        self.assertContains(response, "Fix login")
        self.assertContains(response, "testworker")

    def test_task_create_view(self):
        response = self.client.post(
            reverse("task-create"),
            {
                "name": "New task",
                "description": "New task description",
                "deadline": "2026-08-25",
                "is_completed": False,
                "priority": Task.Priority.MEDIUM,
                "task_type": self.task_type.pk,
                "assignees": [self.worker.pk],
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Task.objects.filter(name="New task").exists()
        )

    def test_task_update_view(self):
        response = self.client.post(
            reverse("task-update", args=[self.task.pk]),
            {
                "name": "Updated task",
                "description": "Updated description",
                "deadline": "2026-08-30",
                "is_completed": True,
                "priority": Task.Priority.LOW,
                "task_type": self.task_type.pk,
                "assignees": [self.worker.pk],
            },
        )

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()

        self.assertEqual(self.task.name, "Updated task")
        self.assertEqual(self.task.priority, Task.Priority.LOW)
        self.assertTrue(self.task.is_completed)

    def test_task_delete_view(self):
        response = self.client.post(
            reverse("task-delete", args=[self.task.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(pk=self.task.pk).exists()
        )
