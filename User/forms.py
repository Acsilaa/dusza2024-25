from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    def is_valid(self):
        return True
    def username_clean(self):
        username = self.data.get("username")
        new = User.objects.filter(username=username)
        if new.count() < 1:
            self.add_error("username","User Does Not Exist")
        return username

    def login(self):
        user = authenticate(username=self.username_clean(), password=self.password_clean())
        print("asd")
        print(user)
        if user is None:
            raise ValidationError("Password don't match")
        return user
    def password_clean(self):
        password = self.cleaned_data['password']
        return password

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
        )
        return user
