from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from category.models import Category
from .forms import TeamForm

def register(request):
    if request.method == "GET":
        return showForm(request)
    elif request.method == "POST":
        return processRequest(request)

def showForm(request):
    form = UserCreationForm()
    return render(request, 'register.html', {"form":form})

def processRequest(request): #POST
    pass