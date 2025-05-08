from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def toggle_completion(self):
        """
        Toggle the completion status of the task.
        If the task is completed, set it to False, otherwise set it to True.
        """
        self.completed = not self.completed
        self.save()
