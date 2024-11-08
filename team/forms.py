from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from category.models import Category
from language.models import Language
from school.models import School

from .models import Team

class TeamCreationForm(forms.Form):
    name = forms.CharField(label='Csapat neve', min_length=5, max_length=150)#unique
    contestant1_name = forms.CharField(label='1. versenyző neve',min_length=5, max_length=150 )
    contestant1_grade = forms.DecimalField(label='1. versenyző évfolyama', decimal_places=0,max_digits=2,min_value=1)
    contestant2_name = forms.CharField(label='2. versenyző neve',min_length=5, max_length=150 )
    contestant2_grade = forms.DecimalField(label='2. versenyző évfolyama', decimal_places=0,max_digits=2 ,min_value=1)
    contestant3_name = forms.CharField(label='3. versenyző neve',min_length=5, max_length=150 )
    contestant3_grade = forms.DecimalField(label='3. versenyző évfolyama', decimal_places=0,max_digits=2 ,min_value=1)
    contestant4_name = forms.CharField(label='Póttag neve',min_length=5, max_length=150,required=False )
    contestant4_grade = forms.DecimalField(label='Póttag évfolyama', decimal_places=0,max_digits=2 ,min_value=1,required=False)
    school = forms.ModelChoiceField(label="Iskola", queryset=School.objects.all(),initial=Category.objects.first())
    teachers = forms.CharField(label='Felkészítő tanár neve',min_length=5, max_length=150 )
    category =  forms.ModelChoiceField(label="Kategória",queryset=Category.objects.all(),initial=Category.objects.first())
    language =  forms.ModelChoiceField(label="Nyelv",queryset=Language.objects.all(),initial=Category.objects.first())
    def check(self):
        name = self.cleaned_data['name']
        new = Team.objects.filter(name=name)
        if new.count():
            self.add_error("name", "Ez a név már létezik.")
            return False
        if self.cleaned_data['contestant4_name'] and self.cleaned_data['contestant4_grade'] is None:
            self.add_error("contestant4_grade", "Póttag évfolyama hiányzik")
            return False
        return True
    def name_clean(self):
        name = self.cleaned_data['name']
        new = Team.objects.filter(name=name)
        if new.count():
            raise ValidationError("Name Already Exist")
        return name

    def save(self,request, commit=True):
        team = Team.objects.create(
            name=self.cleaned_data['name'],
            contestant1_name=self.cleaned_data['contestant1_name'],
            contestant1_grade=self.cleaned_data['contestant1_grade'],
            contestant2_name=self.cleaned_data['contestant2_name'],
            contestant2_grade=self.cleaned_data['contestant2_grade'],
            contestant3_name=self.cleaned_data['contestant3_name'],
            contestant3_grade=self.cleaned_data['contestant3_grade'],
            contestant4_name=self.cleaned_data['contestant4_name'],
            contestant4_grade=self.cleaned_data['contestant4_grade'],
            teachers=self.cleaned_data['teachers'],
            school=self.cleaned_data['school'],
            user=request.user,
            category=self.cleaned_data['category'],
            language=self.cleaned_data['language'],
        )
        return team