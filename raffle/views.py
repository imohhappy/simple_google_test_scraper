from django.shortcuts import render
from .forms import Login, Create


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def phones(request):
    return render(request, 'phones.html')


def electronics(request):
    return render(request, 'electronics.html')


def login(request):
    form = Login()
    return render(request, 'login.html', {'form': form})


def create(request):
    form = Create()
    return render(request, 'create.html', {'form': form})

