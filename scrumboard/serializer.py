from .models import Contact, FreeColor, Subtask, Task, UserDefCategory
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserDefCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefCategory
        fields = '__all__'


class FreeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeColor
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'