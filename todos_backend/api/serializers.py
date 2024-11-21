# contacts/serializers.py
import re
from rest_framework import serializers
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','name', 'email', 'phone'] # optional, was im Input und was im Output angezeigt werden soll

    def validate_phone(self, value):
        if not re.fullmatch(r'^\+?[0-9]+$', str(value)):
            raise serializers.ValidationError(
                "Phone number is not valid. It should contain only numbers and may start with a '+'."
            )
        return value
    
    def validate_email(self, value):
        if not re.fullmatch(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
            raise serializers.ValidationError(
                "Email address is not valid."
            )
        return value
