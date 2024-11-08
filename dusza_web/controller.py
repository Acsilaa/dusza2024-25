from django.shortcuts import render
from urllib.request import Request
from django.shortcuts import render, redirect
from category.models import Category
from team.forms import UserForm

def view(request, path="index"):
    return render(request, f'{path}.html')

def registerUser(request):
    form = UserForm(request.GET)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    context = {'form': form}
    data = {}
    # get options (category, schools, languages)
    categories = list(Category.objects.values())
    data["categories"] = categories
    print(categories)
    return render(request, f'register.html', context)

