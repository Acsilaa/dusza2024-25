from django import forms
from django.contrib.auth.forms import User
from dusza_web.settings import UNIFIED_MAX_LENGTH,UNIFIED_MIN_LENGTH
from .models import School
from django.core.exceptions import ValidationError

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
    username=forms.CharField(label="Igazgató felhasználóneve:", max_length=UNIFIED_MAX_LENGTH,min_length=UNIFIED_MIN_LENGTH)

    password1 = forms.CharField(label='Igazgató jelszava', min_length=UNIFIED_MIN_LENGTH, widget=forms.PasswordInput,
                                max_length=UNIFIED_MAX_LENGTH)
    password2 = forms.CharField(label='Igazgató jelszavának megerősítése', min_length=UNIFIED_MIN_LENGTH, widget=forms.PasswordInput,
                                max_length=UNIFIED_MAX_LENGTH)
    name = forms.CharField(label="Iskola neve", max_length=UNIFIED_MAX_LENGTH+100, min_length=UNIFIED_MIN_LENGTH)
    address = forms.CharField(label="Iskola címe", max_length=UNIFIED_MAX_LENGTH+100, min_length=UNIFIED_MIN_LENGTH)
    contact_name = forms.CharField(label="Kapcsolattartó neve", max_length=UNIFIED_MAX_LENGTH, min_length=UNIFIED_MIN_LENGTH)
    contact_email = forms.EmailField(label="Kapcsolattartó email címe",  min_length=UNIFIED_MIN_LENGTH)
    def prepare(self):
        if self.data.get("name") != "":
            self.fields.pop("username")
            self.fields.pop("password1")
            self.fields.pop("password2")
            pass

    def check(self,request):
        name = self.cleaned_data['name']
        new = School.objects.filter(name=name).first()
        if new and new.id != School.objects.filter(user=request.user).first().id:
            self.add_error("name", "Ilyen iskola névvel már létezik iskola!")
            return False
        address = self.cleaned_data['address']
        new = School.objects.filter(address=address).first()
        if new and new.id != School.objects.filter(user=request.user).first().id:
            self.add_error("address", "Ilyen iskola címmel már létezik iskola!")
            return False
        username = self.cleaned_data['username']
        new = School.objects.filter(username=username).first()
        if new:
            self.add_error("username", "Ilyen felhasználó már létezik!")
            return False
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "A két jelszó nem egyezik!")
            return False
        return True
    def update(self,request):
        school = School.objects.filter(user=request.user).update(
            name=self.cleaned_data['name'],
            address=self.cleaned_data['address'],
            contact_name=self.cleaned_data['contact_name'],
            contact_email=self.cleaned_data['contact_email'],
        )
        return school
    def save(self,request, commit=True):
        user=User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"],
        )
        school = School.objects.create(
            name=self.cleaned_data['name'],
            address=self.cleaned_data['address'],
            contact_name=self.cleaned_data['contact_name'],
            contact_email=self.cleaned_data['contact_email'],
            user=user,
        )
        return school