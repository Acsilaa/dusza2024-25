from django.shortcuts import render,redirect
from school.models import School

from .forms import SchoolCreationForm
from django.contrib import messages

def registerSchool(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Organiser":
        return redirect('login')
    form = SchoolCreationForm(request.GET)
    if request.method == "POST":
        form = SchoolCreationForm(request.POST)
        if form.is_valid() and form.check(request):
            form.save(request)
            messages.success(request, 'Sikeresen regisztrálva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)
def modifySchool(request):
    # check for login
    if not request.user.username or request.user.groups.all()[0].name != "Principal":
        return redirect('login')
    school=School.objects.filter(user=request.user).first()
    form = SchoolCreationForm({
        "name":school.name,
        "address":school.address,
        "contact_name":school.contact_name,
        "contact_email":school.contact_email,
    })
    form.prepare()
    if request.method == "POST":
        form = SchoolCreationForm(request.POST)
        form.prepare()
        if form.is_valid() and form.check(request):
            form.update(request)
            messages.success(request, 'Sikeresen módosítva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)
