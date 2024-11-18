import re
from django.core.exceptions import ValidationError
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    handy = models.CharField(max_length=20)