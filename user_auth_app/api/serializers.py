# api/serializer.py
from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


class RegistrationsSerializer(serializers.ModelSerializer):
    # Wiederholungspasswort nur zum Schreiben
    repeated_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'repeated_password', 'first_name', 'last_name']  # Vorname und Nachname hinzugefügt
        extra_kwargs = {
            'password': {
                'write_only': True  # Passwort wird nur geschrieben, nicht zurückgegeben
            },
        }

    def validate(self, data):
        """ Prüft, ob Passwort und Wiederholungspasswort übereinstimmen. """
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError({'error': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        """ Erstellt einen neuen Benutzer """
        validated_data.pop('repeated_password')  # Wiederholungspasswort entfernen, da es nicht zum Modell gehört

        # Vorname und Nachname aus den übergebenen Daten extrahieren
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        
        # Der Benutzername wird als Kombination von Vorname und Nachname gebildet
        username = f"{first_name} {last_name}" if last_name else first_name  # Wenn kein Nachname angegeben wurde, nur den Vornamen verwenden

        # Benutzer erstellen
        user = User(
            first_name=first_name,  # Vorname setzen
            last_name=last_name,    # Nachname setzen
            username=username,      # Benutzername setzen
            email=email             # E-Mail setzen
        )
        user.set_password(validated_data['password'])  # Passwort verschlüsseln
        user.save()  # Benutzer speichern
        return user
