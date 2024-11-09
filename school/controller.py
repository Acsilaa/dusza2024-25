from django.shortcuts import render,redirect
from .forms import SchoolCreationForm

def registerSchool(request):
    form = SchoolCreationForm(request.GET)
    if request.method == "POST":
        form = SchoolCreationForm(request.POST)
        if form.is_valid() and form.check():
            form.save(request)
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)
