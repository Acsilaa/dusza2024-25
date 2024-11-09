from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def registerUser(request):
    # if already logged in
    if request.user.username:
        return redirect("index")
    form = CustomUserCreationForm(request.GET)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sikeresen regisztrálva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)

def loginUser(request):
    #if already logged in
    if request.user.username:
        return redirect("index")
    form = CustomUserLoginForm(request.POST or None)
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST,{"username":request.POST["username"],"password":request.POST["password"]})
        if form.is_valid():
            login(request, form.login())
            return redirect("index")
    context = {'form': form}
    isError = form.errors
    context['formerror'] = "Rossz felhasználónév vagy jelszó." if isError else None
    return render(request, f'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect("index")