from rest_framework import serializer
from .models import Task


class TaskSerializer(serializer.ModelSerializer):
    class Meta:
        model = "task"
        # fields = ("id", "title", "description", "done")
        fields = "__all__"
