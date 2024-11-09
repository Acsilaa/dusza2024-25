"""
URL configuration for dusza_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template

from . import controller
from django.contrib import admin
from django.urls import path
from User import controller as user
from team import controller as team
from school import controller as school
from contest import controller as contest
from category import controller as category
from language import controller as language
from django.contrib.auth.views import LoginView, LogoutView
controller.initDB()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user.registerUser,name='register'),
    path('login/', user.loginUser,name='login'),
    #logined
    path('logout/', user.logoutUser,name='logout'),
    #contestant
    path('team/register/', team.registerTeam,name='team.register'),
    path('team/missing/', team.missingIndex,name='team.missingIndex'),
    path('team/edit/', team.modifyTeam,name='team.modify'),
    #principal
    path('team/approve/<int:id>/', team.approveTeam,name='team.approve'),
    path('school/edit/', school.modifySchool,name='school.modify'),
    #organiser
    path('team/', team.index,name='team.index'),
    path('team/more/<int:id>/', team.more,name='team.more'),
    path('team/download/<int:id>/', team.download,name='team.download'),
    path('team/approveJoin/<int:id>/', team.approveJoin,name='team.team.approveJoin'),

    path('school/', school.index,name='school.index'),
    path('school/register', school.registerSchool, name='school.register'),

    path('category/add/', category.addCategory,name='category.add'),
    path('category/remove/', category.removeCategory,name='category.remove'),

    path('language/add/',language.addLanguage,name='language.add'),
    path('language/remove/',language.removeLanguage,name='language.remove'),

    path('organiser/change_dl', contest.change_dl, name='organiser.change_dl'),
    path('organiser/toggle_dl_close', contest.toggle_close, name='organiser.toggle_dl_close'),



    path('', controller.render_view,name='index'),
]