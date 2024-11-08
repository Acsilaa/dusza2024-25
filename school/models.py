from django.db import models

# Create your models here.
class School(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=300, unique=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)