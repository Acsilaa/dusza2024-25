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
    path('team/edit/', team.modifyTeam,name='team.modify'),
    #principal
    path('team/approve/', team.modifyTeam,name='team.approve'),
    path('school/edit/', school.modifySchool,name='school.modify'),
    #organiser
    



    path('', controller.render_view,name='index'),
]
"""
path('team/', school.registerSchool,name='team.index'),
    path('team/download', school.registerSchool,name='school.register'),
    path('team/missing', school.registerSchool,name='school.register'),

    path('school/', school.registerSchool,name='school.register'),
    path('school/register', school.registerSchool,name='school.register'),

    path('contest/update/', lambda x: x,name='contest.update'),
    path('contest/close/', lambda x: x,name='contest.close'),

    path('category/add/', lambda x: x,name='category.add'),
    path('category/remove/', lambda x: x,name='category.remove'),
    path('language/add/',lambda x: x,name='language.add'),
    path('language/remove/',lambda x: x,name='language.remove'),
"""