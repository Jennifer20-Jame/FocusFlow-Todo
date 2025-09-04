from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    PRIORITY_CHOICE = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    CATEGORY_CHOICE = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('school', 'School'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title