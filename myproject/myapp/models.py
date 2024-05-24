from django.utils import timezone
from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=10)
    details=models.TextField(max_length=100)
    date=models.DateTimeField(default=timezone.now)