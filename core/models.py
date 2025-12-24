from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    username = models.CharField(max_length=14)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
