from django.db import models
from django.contrib.auth.models import User

class MaintenanceRequest(models.Model):
    CATEGORY_CHOICES = [
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
        ('HVAC', 'HVAC'),
        ('Carpentry', 'Carpentry'),
        ('IT', 'IT'),
        ('Other', 'Other'),
    ]
    
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.status}"
