from urllib.request import Request
from django.shortcuts import render,redirect
from school.models import School
from team.models import Team
from .forms import TeamCreationForm,TeamApprovalForm,TeamMissingForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator

from django.core.files.uploadedfile import SimpleUploadedFile
import csv

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
    print(team.missing)
    if team.missing == "" or team.missing is None:
        return redirect('index')
    context = {'message': team.missing}
    #TODO html
    return render(request, f'contestant/missing.html', context)
def more(request,id):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    team = Team.objects.get(pk=id)
    if (team is None):
        return redirect('index')
    context={}
    team.user = None
    context['team'] = [
        team.name,
        team.school.name,
        team.contestant1_name,
        team.contestant1_grade,
        team.contestant2_name,
        team.contestant2_grade,
        team.contestant3_name,
        team.contestant3_grade,
        team.contestant4_name,
        team.contestant4_grade,
        team.teachers,
        team.category.name,
        team.language.name,
        team.id
    ]
    context["state"] = "Regisztrált"
    if (team.approved):
        context["state"] = "Iskola által jóváhagyva"
    if (team.joined):
        context["state"] = "Szervezők által jóváhagyva"
    form = TeamMissingForm()
    if request.method == "POST":
        form = TeamMissingForm(request.POST)
        if form.is_valid():
            if form.save(request, id):
                messages.success(request, 'Sikeresen elküldve!')
                return redirect("index")
    context["form"] = form
    return render(request, f'organiser/team.html', context)
def index(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    teams = Team.objects.all().order_by('name')
    p = Paginator(teams, 1)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context = {'teams': page_obj}
    return render(request, f'organiser/teams.html', context)
def download(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    teams = Team.objects.all()
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="csapatok.csv"'},
    )

    writer = csv.writer(response)
    for team in teams:
        if team.contestant4_name == "":
            team.contestant4_name = "Nincs"
            team.contestant4_grade = "Nincs"
        writer.writerow([
            team.name,
            team.school,
            team.contestant1_name,
            team.contestant1_grade,
            team.contestant2_name,
            team.contestant2_grade,
            team.contestant3_name,
            team.contestant3_grade,
            team.contestant4_name,
            team.contestant4_grade,
            team.teachers,
            team.category,
            team.language,
        ])

    return response
def approveJoin(request,id):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    team = Team.objects.get(pk=id)
    if (team is None):
        return redirect('index')
    team.joined = True
    messages.success(request,"Sikeresen jóváhagyva!")
    team.save()
    return redirect('team.index')