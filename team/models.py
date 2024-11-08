from django.db import models
from django.contrib.auth.models import User
from language.models import Language
from school.models import School
from category.models import Category
# Create your models here.
class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    school = models.ForeignKey(to=School ,on_delete=models.CASCADE)
    contestant1_name = models.CharField(max_length=100)
    contestant1_grade = models.DecimalField(max_digits=2, decimal_places=0)
    contestant2_name = models.CharField(max_length=100)
    contestant2_grade = models.DecimalField(max_digits=2, decimal_places=0)
    contestant3_name = models.CharField(max_length=100)
    contestant3_grade = models.DecimalField(max_digits=2, decimal_places=0)
    contestant4_name= models.CharField(max_length=100,null=True)
    contestant4_grade = models.DecimalField(max_digits=2,decimal_places=0,null=True)
    teachers = models.TextField()
    category = models.ForeignKey(to=Category ,on_delete=models.CASCADE)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user