import os

from django.conf import settings

import pytest

# Ensure the Django settings module is set
if not settings.configured:
    os.environ['DJANGO_SETTINGS_MODULE'] = (
        'todo.settings'  # Update with your actual project name
    )
    import django

    django.setup()


# You can also add shared fixtures here
@pytest.fixture
def sample_task():
    from tasks.models import Task

    return Task.objects.create(title="Sample Task", completed=False)
