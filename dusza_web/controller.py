from django.shortcuts import render

def view(request, path="index"):

    return render(request, f'{path}.html')