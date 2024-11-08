from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=300, unique=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name