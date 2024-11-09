from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect
from school.models import School

from django.contrib import messages
from category.models import Category


def addCategory(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    if request.method == "POST" and request.POST.get("category") is not None:
        if request.POST.get("category")!="":
            Category.objects.create(name=request.POST.get("category"))
            return JsonResponse({"result": "success", 'cat': request.POST.get("category")})
    return JsonResponse({"result":"failed"})

def removeCategory(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    if request.method == "POST" and request.POST.get("category") is not None:
        if request.POST.get("category")!="":
            Category.objects.filter(name=request.POST.get("category")).first().delete()
            return JsonResponse({"result": "success"})
    return JsonResponse({"result": "failed"})