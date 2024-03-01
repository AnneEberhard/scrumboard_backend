
from rest_framework import serializers
from contacts.models import Contact


"""
This serializer handles the contacts
"""
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'