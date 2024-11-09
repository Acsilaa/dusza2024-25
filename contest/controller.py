from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import redirect
from contest.models import Contest
import json
import datetime

# Create your views here.
def change_dl(request):
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('/login')
    
    # check if date is valid (not past)
    
    d = str(request.POST['deadline'])
    print(d)
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])
    hour = int(d[11:13])
    minute = int(d[14:16])
    _date = datetime.datetime(year, month, day, hour, minute)
    if _date < datetime.datetime.now():
        request.session['dl_form_error'] = "Rossz dátum."
        return redirect('/')
    #set it in db
    obj = Contest.objects.first()
    obj.join_deadline = _date
    obj.save() 
    try:
        del request.session['dl_form_error']
    except:
        pass
    return redirect('/')


def toggle_close(request):
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('/login')
    obj = Contest.objects.first()
    obj.joining_closed = not Contest.objects.first().joining_closed
    obj.save()

    return redirect('/')