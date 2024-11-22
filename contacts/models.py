from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    due_date = models.DateField()
    
    PRIORITY_CHOICES = [
        ('urgent', 'Urgent'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low',
    )

    subtasks = models.CharField(max_length=50)