from urllib.request import Request
from django.shortcuts import render,redirect
from school.models import School
from team.models import Team
from .forms import TeamCreationForm,TeamApprovalForm,TeamMissingForm
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile

def registerTeam(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Contestant":
        return redirect('login')
    
    # if already has a team
    if Team.hasTeam(request.user): 
        return redirect('index')
    
    form = TeamCreationForm(request.GET)
    if request.method == "POST":
        form = TeamCreationForm(request.POST)
        if form.is_valid() and form.check(request):
            form.save(request)
            messages.success(request, 'Sikeresen regisztrálva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'team_register.html', context)
def modifyTeam(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Contestant":
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
        if form.is_valid() and form.check(request):
            form.update(request)
            messages.success(request, 'Sikeresen módosítva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'team_edit.html', context)

def approveTeam(request,id):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Principal":
        return redirect('login')
    school=School.objects.get(user=request.user)
    # if team already approved or team is not in school
    team = Team.objects.get(pk=id)
    if team.approved or team.school_id != school.id:
        return redirect('index')
    form = TeamApprovalForm()
    if request.method == "POST":
        form = TeamApprovalForm(request.POST,request.FILES)
        if form.is_valid() and form.check():
            form.save(request,id)
            messages.success(request, 'Sikeresen jóváhagyva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'principal/team_approve.html', context)
def missingIndex(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Contestant":
        return redirect('login')
    team = Team.objects.get(user=request.user)
    # if team already has a missing
    if team.missing == "" or team.missing is None:
        return redirect('index')
    context = {'message': team.missing}
    #TODO html
    return render(request, f'organiser/team_missing.html', context)
def missing(request,id):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    team = Team.objects.get(pk=id)
    # if team already has a missing
    if team.missing != "" or team.missing is not None:
        return redirect('index')
    form = TeamMissingForm()
    if request.method == "POST":
        form = TeamMissingForm(request.POST)
        if form.is_valid():
            form.save(request, id)
            messages.success(request, 'Sikeresen elküldve!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'organiser/team_missing.html', context)