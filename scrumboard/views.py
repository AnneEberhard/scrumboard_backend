from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from scrumboard.serializer import ContactSerializer, SubTaskSerializer, TaskSerializer, UserDefCategorySerializer, UserSerializer
from .models import Contact, Subtask, Task, UserDefCategory
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

class ContactView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

   
class TaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserDefCategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserDefCategory.objects.all()
    serializer_class = UserDefCategorySerializer  
  

class SubtaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer   
 

class LoginView(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email}) 
    

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.auth.delete()
        return Response({'message': 'Logout erfolgreich'}, status=status.HTTP_200_OK)


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer 


class ForgotView(APIView):
    def post(self, request):
        email = request.data.get('email', None)

        if not email:
            return Response({'error': 'E-Mail-Adresse fehlt'}, status=400)

        try:
            user = User.objects.get(email=email)
            return Response({'exists': True}, status=200)
        except User.DoesNotExist:
            return Response({'exists': False}, status=200)
