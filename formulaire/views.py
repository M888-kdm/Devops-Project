from django.shortcuts import render
from django.http import HttpResponse
from .models import Utilisateur

# Create your views here.
def index(request):
    return HttpResponse('<h1>Bonjour dans le projet de devops</h1> ')


def user_list(request):
    # Query the database to fetch all user records
    users = Utilisateur.objects.all()
    return render(request, 'formulaire/user_list.html', {'users': users})


from django.shortcuts import render
from django.http import HttpResponse

def visit_count(request):
    # Increment the count of visits
    # You can store the count in a database or cache
    # For example, using Django's cache framework:
    from django.core.cache import cache
    count = cache.get('visit_count', 0)
    count += 1
    cache.set('visit_count', count)

    # Return a response to the user
    return HttpResponse(f'<h2>This website has been visited {count} times.</h2>')
