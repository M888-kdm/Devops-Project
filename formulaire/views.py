
from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur

# variable pour stocker les nombres de visites de chaque url
visit_count_users= 0
visit_count_index=0
# Create your views here.
def index(request):
    global visit_count_index
    visit_count_index +=1
    return HttpResponse('<h1>Bonjour dans le projet de devops</h1> ')

def user_list(request):
    global visit_count_users  # variable globale pour visit_count
    visit_count_users += 1

    # fetch tous les records de ma bases de donnees
    users = Utilisateur.objects.all()
    return render(request, 'formulaire/user_list.html', {'users': users, 'visit_count_users': visit_count_users})

def get_visit_count(request):
    global visit_count_users
    global visit_count_index
    return render(request, 'formulaire/visit_count.html', {'visit_count_users': visit_count_users, 'visit_count_index':visit_count_index})




