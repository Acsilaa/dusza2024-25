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
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin', admin.site.urls),
    path('register', user.registerUser,name='register'),
    path('logout', user.logoutUser,name='logout'),
    path('login', user.loginUser,name='login'),
    path('team/register', team.registerTeam,name='team'),

    path('<str:path>', controller.view),
    path('', controller.view,name='index'),
]
