from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def view_details(request):
    return render(request, 'view.html')
# Create your views here.
