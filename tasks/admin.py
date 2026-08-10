from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Position, Worker, TaskType, Task


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("id", "username", "email", "position", "is_staff")
    list_filter = ("position", "is_staff", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        ("Task information", {"fields": ("position",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Task information", {"fields": ("position",)}),
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "task_type",
        "deadline",
        "is_completed",
        "priority",
    )
    list_filter = ("task_type", "is_completed", "priority")
