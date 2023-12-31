from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length = 20,unique=True)
    verified =models.BooleanField(default=False)
    def __str__(self):
        return self.phone_number