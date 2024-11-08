from django.shortcuts import render
from category.models import Category
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def registerUser(request):
    form = CustomUserCreationForm(request.GET)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("index") #TODO
        else:
            print(form.errors)
    context = {'form': form}
    data = {}
    # get options (category, schools, languages)
    categories = list(Category.objects.values())
    data["categories"] = categories
    print(categories)
    return render(request, f'register.html', context)

def loginUser(request):
    form = CustomUserLoginForm(request.POST or None)
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST,{"username":request.POST["username"],"password":request.POST["password"]})
        if form.is_valid():
            login(request, form.login())

            return redirect("index")
    context = {'form': form}
    return render(request, f'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("index")