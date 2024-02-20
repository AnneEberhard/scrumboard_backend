from .models import Contact, Subtask, Task, UserDefCategory
from rest_framework import serializers
from django.contrib.auth.models import User

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



class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

