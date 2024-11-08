from urllib.request import Request
from django.shortcuts import render, redirect

def view(request, path="index"):
    return render(request, f'{path}.html')

