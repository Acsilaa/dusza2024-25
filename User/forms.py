from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from dusza_web.settings import UNIFIED_MIN_LENGTH, UNIFIED_MAX_LENGTH

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages["invalid_login"] = "Kérlek írj be egy jó felhasználónév és jelszó kombinációt. Fontos: mind a kettő mező kis- és nagybetű érzékeny."
    username = forms.CharField(label='Felhasználónév', min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH)
    password = forms.CharField(label='Jelszó',min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH, widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count() < 1:
            self.add_error("username","A felhasználó nem létezik!")
        return username
    def login(self):
        user = authenticate(username=self.username_clean(), password=self.password_clean())
        if user is None:
            self.add_error("password","A felhasználónév vagy jelszó hibás!")
        return user
    def password_clean(self):
        password = self.cleaned_data['password']
        return password

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # add custom error messages
        for field in self.fields:
            self.fields[field].error_messages.update({
                'required': 'Ez a mező szükséges!',
                'max_length': f"Meghaladta a maximális karakterhatárt ({UNIFIED_MAX_LENGTH})",
                'min_length': f"Nem haladta meg a minimális karakterhatárt ({UNIFIED_MIN_LENGTH})"
            })
    username = forms.CharField(label='Felhasználónév', min_length=UNIFIED_MIN_LENGTH, max_length=UNIFIED_MAX_LENGTH)
    username.error_messages.update({})
    username.error_messages["unique"] = "Egy felhasználó ezzel a felhasználónévvel már létezik."
    password1 = forms.CharField(label='Jelszó', min_length=UNIFIED_MIN_LENGTH,widget=forms.PasswordInput, max_length=UNIFIED_MAX_LENGTH)
    password2 = forms.CharField(label='Jelszó megerősítése', min_length=UNIFIED_MIN_LENGTH,widget=forms.PasswordInput, max_length=UNIFIED_MAX_LENGTH)
    def username_clean(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Ilyen felhasználó már létezik!")
        return username


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("A két jelszó nem egyezik!")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
        )
        my_group = Group.objects.filter(name__contains='Contestant').first()
        my_group.user_set.add(user)
        return user
