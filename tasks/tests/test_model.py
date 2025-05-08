import pytest

from tasks.models import Task


@pytest.mark.django_db
def test_task_model_creation():
    # Create a task instance
    task = Task.objects.create(title="Test Task", completed=False)

    # Assert that the task was created successfully
    assert task.title == "Test Task"
    assert task.completed is False
    assert task.pk is not None  # Make sure it has been saved to the database


@pytest.mark.django_db
def test_task_str_method():
    # Create a task instance
    task = Task.objects.create(title="Test Task", completed=False)

    # Assert that the string representation of the task is correct
    assert (
        str(task) == "Test Task"
    )  # Adjust based on how you defined the __str__ method in your model


@pytest.mark.django_db
def test_task_toggle_completed():
    # Create a task instance
    task = Task.objects.create(title="Test Task", completed=False)

    # Toggle the task's completion status
    task.completed = not task.completed
    task.save()

    # Assert that the task's status is now True
    task.refresh_from_db()  # To refresh the object with the latest database values
    assert task.completed is True
