from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Task
from .serializers import TaskSerializer


def unused_function():
    print("Je ne suis jamais appelé !")


def do_something():
    # temp = 42  # jamais utilisé
    return "OK"


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # Add this line


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
