from django.shortcuts import render

from category.models import Category
from .forms import TeamForm

def register(request):
    if request.method == "GET":
        return showForm(request)
    elif request.method == "POST":
        return processRequest(request)

def showForm(request): #GET
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    data = {}
    # get options (category, schools, languages)
    categories = list(Category.objects.values())
    data["categories"] = categories
    print(categories)
    return render(request, f'register.html', context)

def processRequest(request): #POST
    pass