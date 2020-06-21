from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    return render(request, 'login.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


def home(request):
    return render(request, 'home.html')

# def index(request):
#     return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def whatwe(request):
    return render(request, 'whatwe.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    return render(request, 'report.html')

def paramedics(request):
    return render(request, 'paramedics.html')

def fireservice(request):
    return render(request, 'fire-service.html')
