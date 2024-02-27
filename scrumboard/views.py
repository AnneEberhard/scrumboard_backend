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
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail

"""
This view handles the contacts
"""

class ContactView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


"""
This view handles the tasks
"""   
class TaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


"""
This view handles the user defined categories
"""
class UserDefCategoryView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserDefCategory.objects.all()
    serializer_class = UserDefCategorySerializer  
  
"""
This view handles the subtasks and is linked to a specific tasks
"""
class SubtaskView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer   
 
"""
This view handles login
"""
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
    
"""
This view handles logout
"""
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.auth.delete()
        return Response({'message': 'Logout erfolgreich'}, status=status.HTTP_200_OK)

"""
This view handles registering a new user
"""
class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer 

"""
This view checks if the email send from the frontend is existent in the user db and returns a unique link including a token and a uidb
"""
class ForgotView(APIView):
    def post(self, request):
        email = request.data.get('email', None)

        if not email:
            return Response({'error': 'E-Mail-Adresse fehlt'}, status=400)

        try:
            user = User.objects.get(email=email)

            token_generator = PasswordResetTokenGenerator()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            reset_link = f"http://127.0.0.1:5500/reset.html?uidb64={uidb64}&token={token}"

                        
            subject = 'Passwort zurücksetzen'
            message = f'Hallo {user.username}, klicken Sie auf den folgenden Link, um Ihr JOIN-Passwort zurückzusetzen: {reset_link}'
            from_email = 'noreply@example.com'  
            recipient_list = [user.email]

            send_mail(subject, message, from_email, recipient_list)

            return Response({'exists': True, 'reset_link': reset_link}, status=200)

        except User.DoesNotExist:
            return Response({'exists': False}, status=200)

"""
This view resets the password in the backend with the one entered in the frontend
"""
class PasswordResetConfirmView(APIView):
    def post(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        new_password = request.data.get('password', None)

        uid = urlsafe_base64_decode(uidb64)

        user = User.objects.get(pk=uid)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({'error': 'Ungültiges Token'}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({'success': 'Passwort erfolgreich zurückgesetzt'}, status=200)
    

