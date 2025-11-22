from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.username
    
class Child(models.Model):
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='child_profile_pics/', null=True, blank=True)
    def __str__(self):
        return self.name