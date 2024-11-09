from urllib.request import Request
from django.shortcuts import render,redirect
from team.models import Team
from .forms import TeamCreationForm
from django.contrib import messages

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
            messages.success(request, 'Sikeresen regisztrálva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'team_register.html', context)
def modifyTeam(request):
    # check for login
    if not request.user.username:
        return redirect('login')

    # if does not have a team
    if not Team.hasTeam(request.user):
        return redirect('index')
    team = Team.objects.filter(user=request.user).first()
    form = TeamCreationForm({
        'name': team.name,
        'contestant1_name': team.contestant1_name,
        'contestant1_grade': team.contestant1_grade,
        'contestant2_name': team.contestant2_name,
        'contestant2_grade': team.contestant2_grade,
        'contestant3_name': team.contestant3_name,
        'contestant3_grade': team.contestant3_grade,
        'contestant4_name': team.contestant4_name,
        'contestant4_grade': team.contestant4_grade,
        'school': team.school,
        'teachers': team.teachers,
        'category': team.category,
        'language': team.language,
    })
    if request.method == "POST":
        form = TeamCreationForm(request.POST)
        if form.is_valid() and form.checkForModify():
            form.update(request)
            messages.success(request, 'Sikeresen módosítva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'team_register.html', context)
