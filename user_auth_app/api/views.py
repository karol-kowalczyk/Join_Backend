from rest_framework import generics
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import RegistrationsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationsSerializer(data=request.data)
        if serializer.is_valid():
            saved_account = serializer.save()
            # Token erstellen oder abrufen
            token, created = Token.objects.get_or_create(user=saved_account)
            
            # Antwort-Daten vorbereiten
            data = {
                'token': token.key,  # `.key`, um den eigentlichen Token zu erhalten
                'email': saved_account.email
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            # Fehler zurückgeben
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Benutzer anhand der E-Mail und des Passworts authentifizieren
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,  # Das Token
                'username': user.username,  # Der Benutzername
                'email': user.email  # Optional: E-Mail
            }
            return Response(data)  # Nur Token zurückgeben, ohne Benutzernamen
        else:
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
