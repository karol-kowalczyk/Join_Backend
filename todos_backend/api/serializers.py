# contacts/serializers.py
import re
from rest_framework import serializers
from contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'handy']

    def validate_handy(self, value):
        if not re.fullmatch(r'^\+?[0-9]+$', value):
            raise serializers.ValidationError(
                "Phone number is not valid."
            )
        return value
