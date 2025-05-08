from django.urls import reverse

import pytest
from rest_framework.test import APIClient

from tasks.models import Task


@pytest.mark.django_db
def test_list_tasks():
    Task.objects.create(title="Task 1", completed=False)
    Task.objects.create(title="Task 2", completed=True)

    client = APIClient()
    response = client.get(reverse('task-list'))
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    response = client.post(
        reverse('task-list'), {"title": "New Task", "completed": False}, format="json"
    )
    assert response.status_code == 201
    assert response.data["title"] == "New Task"


@pytest.mark.django_db
def test_retrieve_task():
    task = Task.objects.create(title="Sample", completed=False)
    client = APIClient()
    response = client.get(reverse('task-detail', args=[task.id]))
    assert response.status_code == 200
    assert response.data["title"] == "Sample"


@pytest.mark.django_db
def test_update_task():
    task = Task.objects.create(title="To Update", completed=False)
    client = APIClient()
    response = client.put(
        reverse('task-detail', args=[task.id]),
        {"title": "Updated", "completed": True},
        format="json",
    )
    assert response.status_code == 200
    assert response.data["title"] == "Updated"


@pytest.mark.django_db
def test_delete_task():
    task = Task.objects.create(title="To Delete", completed=False)
    client = APIClient()
    response = client.delete(reverse('task-detail', args=[task.id]))
    assert response.status_code == 204
