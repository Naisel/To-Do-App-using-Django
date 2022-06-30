
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    is_completed = models.BooleanField(default=False)
    create_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_completed']

