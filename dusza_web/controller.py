from urllib.request import Request
from django.shortcuts import render, redirect

def render_view(request, path="index"):
    try:
        return render(request, f'{path}.html')
    except:
        return render(request, f'index.html')

