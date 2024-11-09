from urllib.request import Request
from xmlrpc.client import DateTime

from django.shortcuts import render, redirect
from category.models import Category
from language.models import Language
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
    print("asdf")
    context = {}
    team = list(Team.objects.filter(user=request.user))
    context['hasTeam'] = Team.hasTeam(request.user)
    context['in_deadline'] = Contest.isOpen()

    team = team[0] if team != [] else None
    if(team != None):
        team.id = None
        team.user = None
    context['team'] = team

    print(context['hasTeam'],context['in_deadline'])
    return render(request, 'contestant/home.html', context)



def organiserPanel(request):
    return render(request, 'organiser/home.html')


def principalPanel(request):
    return render(request, 'principal/home.html')