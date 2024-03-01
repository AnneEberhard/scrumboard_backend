from .models import UserDefCategory
from rest_framework import serializers

"""
This serializer handles the categories defined by the users
"""
class UserDefCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefCategory
        fields = '__all__'