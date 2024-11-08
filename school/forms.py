from django import forms
from django.contrib.auth.forms import User

from .models import School

class SchoolCreationForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=10)
    address = forms.CharField(max_length=300, min_length=3)
    contact_name = forms.CharField(max_length=100, min_length=5)
    contact_email = forms.EmailField(max_length=100 , min_length=5)

    def name_clean(self):
        name = self.cleaned_data['name']
        new = School.objects.filter(name=name)
        if new.count():
            self.add_error("name", "Name Already Exist")
        return name
    def check(self):
        name = self.cleaned_data['name']
        new = School.objects.filter(name=name)
        if new.count():
            self.add_error("name", "Name Already Exist")
            return False
        address = self.cleaned_data['address']
        new = School.objects.filter(address=address)
        if new.count():
            self.add_error("address", "Address Already Exist")
            return False
        return True
    def save(self,request, commit=True):
        school = School.objects.create(
            name=self.cleaned_data['name'],
            address=self.cleaned_data['address'],
            contact_name=self.cleaned_data['contact_name'],
            contact_email=self.cleaned_data['contact_email'],
            user=request.user,
        )
        return school