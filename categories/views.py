from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import UserDefCategorySerializer
from .models import UserDefCategory

"""
This view handles the user defined categories
"""
class UserDefCategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserDefCategory.objects.all()
    serializer_class = UserDefCategorySerializer  
