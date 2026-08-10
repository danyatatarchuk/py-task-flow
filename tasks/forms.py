from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
        )
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date"}
            ),
            "description": forms.Textarea(
                attrs={"rows": 4}
            ),
        }
