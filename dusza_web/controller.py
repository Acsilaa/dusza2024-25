from urllib.request import Request
from django.shortcuts import render, redirect
from team.models import Team
from contest.models import Contest

def render_view(request):
    if(request.user.username):
        if(request.user.groups.all()[0].name == "Organiser"):
            return organiserPanel(request)
        if(request.user.groups.all()[0].name == "Principal"):
            return principalPanel(request)
        if(request.user.groups.all()[0].name == "Contestant"):
            return contestantPanel(request)
    return render(request, f'index.html')



def contestantPanel(request):
    context = {}
    team = list(Team.objects.filter(user=request.user))
    context['hasTeam'] = Team.hasTeam(request.user)
    context['in_deadline'] = Contest.isOpen()

    team = team[0] if team != [] else None
    if(team != None):
        team.id = None
        team.user = None
    context['team'] = team


    return render(request, 'contestant/home.html', context)



def organiserPanel(request):
    return render(request, 'organiser/home.html')


def principalPanel(request):
    return render(request, 'principal/home.html')