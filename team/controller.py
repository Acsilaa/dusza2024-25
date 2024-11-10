from urllib.request import Request
from django.shortcuts import render,redirect
from school.models import School
from category.models import Category
from language.models import Language
from team.models import Team
from .forms import TeamCreationForm,TeamApprovalForm,TeamMissingForm
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from dusza_web import settings
import os
from django.core.files.uploadedfile import SimpleUploadedFile
import csv
from django.db.models import Q
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
    context['team'] = team
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
    context["hasApprovalFile"] = team.approval_file not in ["",None]
    return render(request, f'organiser/team.html', context)
def filter(request,models):
    request.GET.get("category")
    if request.GET.get("category") and Category.objects.filter(name__contains=request.GET.get("category").split(";")[0:-1]):
        models = models.filter(category__contains=request.GET.get("category").split(";")[0:-1])
    if request.GET.get("language") and Language.objects.filter(name__contains=request.GET.get("language").split(";")[0:-1]):
        models = models.filter(language__contains=request.GET.get("language").split(";")[0:-1])
    if request.GET.get("contestant4") == "Nincs":
        models = models.exclude(contestant4_grade__isnull=True)
    state_r="regisztralt"
    state_i="iskola altal jovahagyva"
    state_s="szervezok altal jovahagyva"
    if request.GET.get("state"):
        match request.GET.get("state").split(";")[0:-1]:
            case [state_r]:
                models = models.filter(Q(approved=False) & Q(joined=False))
            case [state_i]:
                models = models.filter(Q(approved=True) & Q(joined=False))
            case [state_s]:
                models = models.filter(Q(approved=True) & Q(joined=True))
            case [state_r,state_i]:
                models = models.filter(joined=False)
            case [state_i,state_s]:
                models = models.filter(approved=True)
            case [state_r,state_s]:
                models = models.filter(Q(approved=False) | Q(joined=True))
    return models

def index(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    teams = Team.objects.all().order_by("-date_modified")
    context = {}
    #filter
    context["category"] = Category.objects.all()
    context["language"] = Language.objects.all()
    teams = filter(request, teams)

    p = Paginator(teams, 1)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    context['teams']= page_obj
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
def approveJoin(request,id,is_approve):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    team = Team.objects.get(pk=id)
    if (team is None):
        return redirect('index')
    if is_approve == "approve":
        team.joined = True
        print("sf")
        messages.success(request,"Sikeresen jóváhagyva!")
    elif is_approve == "disapprove":
        team.joined = False
        messages.success(request, "Sikeresen visszavonva!")
    team.save()
    return redirect('team.index')
def downloadApproval(request,id):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    team = Team.objects.get(pk=id)
    if (team is None):
        return redirect('index')
    print(settings.MEDIA_ROOT,team.approval_file.name)
    file_path = os.path.join(settings.MEDIA_ROOT,team.approval_file.name)
    print(file_path)
    if os.path.exists(file_path):
        print("asd")
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404