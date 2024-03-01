from .models import Category
from rest_framework import serializers

"""
This serializer handles the categories defined by the users
"""
class CategoryViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'colorCode']
        #fields = '__all__'