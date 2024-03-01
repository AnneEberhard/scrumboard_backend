from .models import  Task
from rest_framework import serializers


"""
This serializer handles the tasksFC
"""
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
