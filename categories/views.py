from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializer import CategoryViewSetSerializer
from .models import Category

"""
This view handles the user defined categories
"""
class CategoryViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryViewSetSerializer

