from django.db import models
from django.contrib.auth.models import User
from dusza_web.settings import UNIFIED_MAX_LENGTH,UNIFIED_MIN_LENGTH
# Create your models here.
class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=UNIFIED_MAX_LENGTH+100, unique=True)
    address = models.CharField(max_length=UNIFIED_MAX_LENGTH+100, unique=True)
    contact_name = models.CharField(max_length=UNIFIED_MAX_LENGTH)
    contact_email = models.CharField(max_length=UNIFIED_MAX_LENGTH)

    def __str__(self) -> str:
        return self.name