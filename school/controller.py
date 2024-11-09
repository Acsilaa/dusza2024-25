from django.shortcuts import render,redirect
from .forms import SchoolCreationForm
from django.contrib import messages

def registerSchool(request):
    form = SchoolCreationForm(request.GET)
    if request.method == "POST":
        form = SchoolCreationForm(request.POST)
        if form.is_valid() and form.check():
            form.save(request)
            messages.success(request, 'Sikeresen regisztrálva!')
            return redirect("index")
    context = {'form': form}
    return render(request, f'register.html', context)
