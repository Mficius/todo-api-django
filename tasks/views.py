# import math  # inutilisé dans le fichier

from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def unused_function():
    print("Je ne suis jamais appelé !")


def do_something():
    # temp = 42  # jamais utilisé
    return "OK"


def greet_user():
    print("Hello, user!")


def greet_admin():
    print("Hello, user!")  # duplication


def complex_function(x):
    if x > 0:
        if x < 10:
            if x % 2 == 0:
                if x % 3 == 0:
                    return "Divisible by 6"
    return "Other"


def add_numbers(a, b):
    result = a + b
    return result


def divide(a, b):
    return a / b  # peut échouer si b == 0
