from django.db import models
from django.contrib.auth.models import User
from language.models import Language
from school.models import School
from category.models import Category
from dusza_web.settings import UNIFIED_MAX_LENGTH,UNIFIED_MIN_LENGTH


# Create your models here.
class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField( max_length=UNIFIED_MAX_LENGTH, unique=True, )
    school = models.ForeignKey(to=School ,on_delete=models.CASCADE)
    contestant1_name = models.CharField(max_length=UNIFIED_MAX_LENGTH)
    contestant1_grade = models.DecimalField(max_digits=2, decimal_places=0,)
    contestant2_name = models.CharField(max_length=UNIFIED_MAX_LENGTH)
    contestant2_grade = models.DecimalField(max_digits=2, decimal_places=0,)
    contestant3_name = models.CharField(max_length=UNIFIED_MAX_LENGTH)
    contestant3_grade = models.DecimalField(max_digits=2, decimal_places=0,)
    contestant4_name= models.CharField(max_length=UNIFIED_MAX_LENGTH,null=True)
    contestant4_grade = models.DecimalField(max_digits=2,decimal_places=0,null=True,)
    teachers = models.TextField(max_length=UNIFIED_MAX_LENGTH)
    category = models.ForeignKey(to=Category ,on_delete=models.CASCADE)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approval_file = models.FileField(upload_to='approval_files/', blank=True, null=True)
    missing=models.CharField(max_length=UNIFIED_MAX_LENGTH, blank=True, null=True)
    joined = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

    def hasTeam(user):
        return list(Team.objects.filter(user=user).all()) != []