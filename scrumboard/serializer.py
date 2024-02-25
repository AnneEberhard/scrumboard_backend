from .models import Contact, Subtask, Task, UserDefCategory
from rest_framework import serializers
from django.contrib.auth.models import User

"""
This serializer handles the contacts
"""
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

"""
This serializer handles the tasks
"""
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

"""
This serializer handles the categories defined by the users
"""
class UserDefCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefCategory
        fields = '__all__'

"""
This serializer handles the subtasks
"""
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'

"""
This serializer handles the user and assures a correct password is created
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create (self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user

"""
This serializer handles the authtokens and is needed for the creation of a correct password
"""
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )
