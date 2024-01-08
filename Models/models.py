from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.

class Account(AbstractUser):

    id_number = models.CharField(max_length=32, unique=True)
    ROLES = (("Teacher", "Teacher"), ("Student", "Student"))
    role = models.CharField(choices = ROLES, max_length=32)
    REQUIRED_FIELDS = ['id_number', 'first_name', 'last_name', 'role']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Ticket(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='ticket_sent')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='ticket_received', limit_choices_to={'role': 'Teacher'})
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now)
    
    STATUSES = (("UC", "Under Consideration",), ("PD", "Pending"), ("DC", "Declined"), ("RS", "Resolved"))
    status = models.CharField(choices=STATUSES, max_length=32)

    class Meta:
        
        unique_together = ('receiver', 'title')
    def __str__(self):
        return f"{self.sender} | {self.title}"




