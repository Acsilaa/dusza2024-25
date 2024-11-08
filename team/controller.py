from urllib.request import Request
from django.shortcuts import render,redirect
from .forms import TeamCreationForm

def registerTeam(request):
    form = TeamCreationForm(request.GET)
    if request.method == "POST":
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("index") #TODO
    context = {'form': form}
    return render(request, f'register.html', context)
