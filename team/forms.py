from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from .models import Team

class TeamCreationForm(forms.Form):
    name = forms.CharField(label='name', min_length=5, max_length=150)
    contestant1_name = forms.CharField(label='password',min_length=5, max_length=150 )
    contestant1_grade = forms.DecimalField(label='password',min_value=9, max_value=15,decimal_places=0,max_length=2 )
    contestant1_grade = forms.DecimalField(label='password',min_value=9, max_value=15,decimal_places=0,max_length=2 )
    contestant1_grade = forms.DecimalField(label='password',min_value=9, max_value=15,decimal_places=0,max_length=2 )

    def name_clean(self):
        name = self.cleaned_data['name'].lower()
        new = User.objects.filter(name=name)
        if new.count():
            raise ValidationError("Name Already Exist")
        return name

    def save(self, commit=True):
        team = Team.objects.create(
            name=self.cleaned_data['name'],
        )
        return team