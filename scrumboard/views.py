from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
from django.contrib.auth.views import PasswordResetConfirmView
from django.middleware.csrf import get_token
from django.views import View


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

            token_generator = PasswordResetTokenGenerator()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            reset_link = f"http://127.0.0.1:5500/reset.html?uidb64={uidb64}&token={token}"

            # TODO: Hier E-Mail-Versand einfügen, z.B., mit Django send_mail

            return Response({'exists': True, 'reset_link': reset_link}, status=200)

        except User.DoesNotExist:
            return Response({'exists': False}, status=200)
        

class CSRFTokenView(View):
    def get(self, request, *args, **kwargs):
        token = get_token(request)
        response = JsonResponse({'csrfToken': token})
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500" 
        response["Access-Control-Allow-Credentials"] = "true"
        return response


class CustomPasswordResetConfirmView(PasswordResetConfirmView):

    def post(self, request, *args, **kwargs):
        print('yes')
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
    
#def custom_password_reset_confirm(request, uidb64, token):
#    try:
#        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
#        user = get_object_or_404(User, pk=uid)
#        
#        if not PasswordResetTokenGenerator().check_token(user, token):
#            return JsonResponse({'error': 'Ungültiges Token'}, status=400)
#
#        if request.method == 'POST':
#            new_password = request.POST.get('password', None)
#            user.set_password(new_password)
#            user.save()
#            return JsonResponse({'success': 'Passwort erfolgreich zurückgesetzt'}, status=200)
#
#    except Exception as e:
#        return JsonResponse({'error': str(e)}, status=400)
#
#    return JsonResponse({'error': 'Ungültige Anfrage'}, status=400)
