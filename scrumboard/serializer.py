from .models import Contact, FreeColor, Task, UserDefCategory
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