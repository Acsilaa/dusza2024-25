from django.db import models

# Create your models here.
class Contest(models.Model):
    join_deadline = models.DateTimeField()
    joining_closed = models.BooleanField(default=False)