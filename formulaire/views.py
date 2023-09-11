
from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur
from django.core.cache import cache

# Create your views here.
def index(request):
    return HttpResponse('<h1>Bonjour dans le projet de devops</h1> ')

def user_list(request):
    visits = cache.get('visits')
    if(visits is None):
        visits = 1
    else:
        visits += 1
    # Get all users from database
    users = Utilisateur.objects.all()
    return render(request, 'formulaire/user_list.html', {'users': users })

def get_visit_count(request):
    visits = cache.get('visits')
    return render(request, 'formulaire/visit_count.html', {'visits': visits})




