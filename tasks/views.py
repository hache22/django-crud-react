from django.contrib import admin
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task


# FUNCIONES QUE RESPONDEN ALGO AL CLIENTE
class TaskView(viewsets.ModelViewSet):
    """
    Esta clase hereda de viewsets.ModelViewSet,
    lo que significa que ya tiene implementada la funcionalidad básica
    para las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en un modelo específico.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
