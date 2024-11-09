from school.models import School
from django.shortcuts import render,redirect
from http.client import HTTPResponse
from django.http import JsonResponse
from django.contrib import messages
from language.models import Language


def addLanguage(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    if request.method == "POST" and request.POST.get("language") is not None:
        if request.POST.get("language")!="":
            Language.objects.create(name=request.POST.get("language"))
            return JsonResponse({"result": "success"})
    return JsonResponse({"result":"failed"})

def removeLanguage(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    if request.method == "POST" and request.POST.get("language") is not None:
        if request.POST.get("language")!="":
            Language.objects.get(name=request.POST.get("language")).delete()
            return JsonResponse({"result": "success"})
    return JsonResponse({"result": "failed"})