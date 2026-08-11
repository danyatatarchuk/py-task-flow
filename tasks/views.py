from django.views.generic import CreateView, DetailView, ListView, UpdateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = "/tasks/"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_update.html"

    def get_success_url(self):
        return f"/tasks/{self.object.pk}/"
