from urllib.request import Request
from django.shortcuts import render, redirect

def render_view(request):
    if(request.user.username):
        if(request.user.groups.all()[0].name == "Organiser"):
            return render(request, 'organiser/home.html')
        if(request.user.groups.all()[0].name == "Principal"):
            return render(request, 'principal/home.html')
        if(request.user.groups.all()[0].name == "contestant"):
            return render(request, 'contestant/home.html')
    return render(request, f'index.html')