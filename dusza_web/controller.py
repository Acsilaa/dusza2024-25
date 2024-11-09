from urllib.request import Request
from xmlrpc.client import DateTime

from django.shortcuts import render, redirect
from category.models import Category
from language.models import Language
from school.models import School
from team.models import Team
from contest.models import Contest
from django.contrib.auth.models import Group

def render_view(request):

    if(request.user.username):
        if(request.user.groups.all()[0].name == "Organiser"):
            return organiserPanel(request)
        if(request.user.groups.all()[0].name == "Principal"):
            return principalPanel(request)
        if(request.user.groups.all()[0].name == "Contestant"):
            return contestantPanel(request)
    return render(request, f'index.html')


def initDB():
    #TODO: debug-ra
    groups=["Organiser","Principal","Contestant"]
    for i in groups:
        if not Group.objects.filter(name=i).exists():
            Group.objects.create(name=i)
    languages=["Python","PHP","C#","JavaScript","Java"]
    for i in languages:
        if not Language.objects.filter(name=i).exists():
            Language.objects.create(name=i)
    categories=["Web","Mobil","Hagyományos"]
    for i in categories:
        if not Category.objects.filter(name=i).exists():
            Category.objects.create(name=i)
    if not Contest.objects.all().exists():
        Contest.objects.create(join_deadline="2025-11-11 11:11")


def contestantPanel(request):
    context = {}
    team = list(Team.objects.filter(user=request.user))
    context['hasTeam'] = Team.hasTeam(request.user)
    context['in_deadline'] = Contest.isOpen()
    context["hasMissing"] = False

    team = team[0] if team != [] else None
    if(team != None):
        if  team.missing != "":
            context["hasMissing"]=True
        elif team.missing is not None:
            context["hasMissing"] =True
        team.id = None
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
        ]
        context["state"] = "Regisztrált"
        if(team.approved):
            context["state"] = "Iskola által jóváhagyva"
        if(team.joined):
            context["state"] = "Szervezők által jóváhagyva"
    return render(request, 'contestant/home.html', context)



def organiserPanel(request):
    deadline = Contest.objects.first().join_deadline
    isClosed = Contest.objects.first().joining_closed
    d = deadline
    d = str(deadline)
    year = d[0:4]
    month =d[5:7]
    day = d[8:10]
    hour = d[11:13]
    minute = d[14:16]
    second = d[17:19]
    dl = f"{year}-{month}-{day}T{hour}:{minute}"
    langs = []
    cats = []
    for l in list(Language.objects.all()):
        langs.append(l.name)
    for c in list(Category.objects.all()):
        cats.append(c.name)
    context = {
        'languages': langs,
        'categories': cats,
        "deadline": dl,
        "is_closed": isClosed,
    }
    try:
        context['dl_form_error'] = request.session['dl_form_error']
    except:
        context['dl_form_error'] = None

    return render(request, 'organiser/home.html', context)


def principalPanel(request):
    context = {}
    school = School.objects.filter(user=request.user).first()
    teams = list(Team.objects.filter(school=school))
    context["teams"]=teams
    context["contact_name"]=school.contact_name
    context["contact_email"]=school.contact_email
    context["address"]=school.address
    context["name"]=school.name
    context["hasTeam"] = teams != []
    return render(request, 'principal/home.html',context)