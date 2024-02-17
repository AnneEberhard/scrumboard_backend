from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from scrumboard.serializer import ContactSerializer, SubTaskSerializer, TaskSerializer, UserDefCategorySerializer
from .models import Contact, Subtask, Task, UserDefCategory
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics

class ContactView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

   
class TaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserDefCategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = UserDefCategory.objects.all()
    serializer_class = UserDefCategorySerializer  
  

class SubtaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer   
 
    

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })  