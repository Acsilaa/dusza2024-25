from django import forms
from django.contrib.auth.forms import User
from dusza_web.settings import UNIFIED_MAX_LENGTH,UNIFIED_MIN_LENGTH
from .models import School

class SchoolCreationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

        # add custom error messages
        for field in self.fields:
            self.fields[field].error_messages.update({
                'required': 'Ez a mező szükséges!',
                'max_length': f"Meghaladta a maximális karakterhatárt ({UNIFIED_MAX_LENGTH})",
                'min_length': f"Nem haladta meg a minimális karakterhatárt ({UNIFIED_MIN_LENGTH})",
                "invalid":f"Megadott érték nem email!",
            })
    name = forms.CharField(label="Iskola neve", max_length=UNIFIED_MAX_LENGTH+100, min_length=UNIFIED_MIN_LENGTH)
    address = forms.CharField(label="Iskola címe", max_length=UNIFIED_MAX_LENGTH+100, min_length=UNIFIED_MIN_LENGTH)
    contact_name = forms.CharField(label="Kapcsolattartó neve", max_length=UNIFIED_MAX_LENGTH, min_length=UNIFIED_MIN_LENGTH)
    contact_email = forms.EmailField(label="Kapcsolattartó email címe",  min_length=UNIFIED_MIN_LENGTH)

    def name_clean(self):
        name = self.cleaned_data['name']
        new = School.objects.filter(name=name)
        if new.count():
            self.add_error("name", "Ilyen iskola névvel már létezik iskola!")
        return name
    def check(self):
        name = self.cleaned_data['name']
        new = School.objects.filter(name=name)
        if new.count():
            self.add_error("name", "Ilyen iskola névvel már létezik iskola!")
            return False
        address = self.cleaned_data['address']
        new = School.objects.filter(address=address)
        if new.count():
            self.add_error("address", "Ilyen iskola címmel már létezik iskola!")
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