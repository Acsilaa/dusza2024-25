from django.shortcuts import render
from school.models import School
from category.models import Category
from language.models import Language

def register(request):
    if request.method == "GET":
        return showForm(request)
    elif request.method == "POST":
        return processRequest(request)

def showForm(request): #GET
    data = {}
    # get options (category, schools, languages)
    categories = list(Category.objects.values())
    data["categories"] = categories
    print(categories)
    return render(request, f'register.html', data)

def processRequest(request): #POST
    pass