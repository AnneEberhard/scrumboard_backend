from .models import Category
from rest_framework import serializers

"""
This serializer handles the categories defined by the users
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'