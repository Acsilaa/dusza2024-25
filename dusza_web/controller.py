from django.shortcuts import render

def view(request):
    print("asd")
    return render(request, 'index.html', {})