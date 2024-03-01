from .models import Subtask
from rest_framework import serializers


"""
This serializer handles the subtasks
"""
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
