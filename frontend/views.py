from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
# Create your views here.
def home_view(request):
    links = YouTubeCoreses.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'frontend/index.html', context)

@login_required(login_url='account_login')
def notes_view(request):
    return render(request, 'frontend/notes.html')
    