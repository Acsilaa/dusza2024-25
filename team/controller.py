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
    form = TeamCreationForm(request.GET)
    form.name=team.name
    form.contestant1_name = team.contestant1_name
    form.contestant1_grade = team.contestant1_grade
    form.contestant2_name = team.contestant2_name
    form.contestant2_grade = team.contestant2_grade
    form.contestant3_name = team.contestant3_name
    form.contestant3_grade = team.contestant3_grade
    form.contestant4_name = team.contestant4_name
    form.contestant4_grade = team.contestant4_grade
    form.school = team.school
    form.teachers = team.teachers
    form.category = team.category
    form.language = team.language
    if request.method == "POST":
        form = TeamCreationForm(request.POST)
        if form.is_valid() and form.check():
            form.update(request)
            messages.success(request, 'Sikeresen módosítva!')
            return redirect("modify.team")
    context = {'form': form}
    return render(request, f'team_register.html', context)
