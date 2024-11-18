# contacts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from contacts.models import Contact
from .serializers import ContactSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class ContactListView(APIView):
    def get(self, request):
        contacts = Contact.objects.all()  # Alle Kontakte abrufen
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Daten aus der Anfrage serialisieren
        serializer = ContactSerializer(data=request.data)
        
        # Überprüfen, ob die Daten valide sind
        if serializer.is_valid():
            serializer.save()  # Neues Objekt speichern
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Fehlerhafte Daten zurückgeben
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)