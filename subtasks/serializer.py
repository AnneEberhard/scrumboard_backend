from .models import Subtask
from rest_framework import serializers


"""
This serializer handles the subtasks
"""
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
