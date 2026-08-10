from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Position, Worker, TaskType


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("id", "username", "email", "position", "is_staff")
    list_filter = ("position", "is_staff", "is_active")


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
