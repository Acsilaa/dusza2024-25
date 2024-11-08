from urllib.request import Request

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from category.models import Category
from .forms import RawTeamForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "GET":
        return showForm(request)
    elif request.method == "POST":
        return processRequest(request)

def showForm(request): #GET
    form = RawTeamForm(request.GET)
    context = {'form': form}
    data = {}
    # get options (category, schools, languages)
    categories = list(Category.objects.values())
    data["categories"] = categories
    print(categories)
    return render(request, f'register.html', context)

def processRequest(request): #POST
    form = RawTeamForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.errors)
    return showForm(request)