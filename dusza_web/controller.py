from urllib.request import Request
from django.shortcuts import render, redirect

def render_view(request):
    return render(request, f'index.html')

