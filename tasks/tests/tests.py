# tests.py
import pytest

from tasks.models import Task


@pytest.mark.django_db
def test_task_toggle_completion():
    # Create a task with `completed` set to False
    task = Task.objects.create(title="Test Task", completed=False)

    # Toggle completion and check the status
    task.toggle_completion()
    assert task.completed is True  # It should be True after toggle

    # Toggle again and check the status
    task.toggle_completion()
    assert task.completed is False  # It should be False again after the second toggle
