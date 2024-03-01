from .serializer import SubtaskSerializer
from .models import Subtask
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets

"""
This view handles the subtasks and is linked to a specific tasks
"""
class SubtaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer   


"""
This view handles the user defined categories
"""
class SubtaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer