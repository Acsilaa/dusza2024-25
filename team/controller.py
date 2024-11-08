from urllib.request import Request
from django.shortcuts import render,redirect
from team.models import Team
from .forms import TeamCreationForm

def registerTeam(request):
    # check for login
    if not request.user.username:
        return redirect('login')
    
    # if already has a team
    if Team.hasTeam(request.user): 
        return redirect('index')
    
    form = TeamCreationForm(request.GET)
    if request.method == "POST":
        form = TeamCreationForm(request.POST)
        if form.is_valid() and form.check():
            form.save(request)
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)
