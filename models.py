# nombre_del_proyecto/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    # Campos adicionales si es necesario
    pass
class Clientes (models.Model):
    nombre=models.CharField(max_length=30)
    email=models.CharField(max_length=50)


from django.contrib.auth.models import User
from django.db import models

class UserNavigationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.path} - {self.timestamp}"
