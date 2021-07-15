from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from jobs.models import *
# Create your views here.
# Create your views here.
def home_view(request):
    job = jobs.objects.all()
    context = {
        'jobs': job,
        
    }
   
    return render(request, 'frontend/index.html')
def about_view(request):
    # links = YouTubeCoreses.objects.all()
    context = {
        # 'links': links,
    }
    return render(request, 'frontend/about.html', context)
def contact_view(request):
    # links = YouTubeCoreses.objects.all()
    context = {
        # 'links': links,
    }
    return render(request, 'frontend/contact.html', context)

@login_required(login_url='account_login')
def notes_view(request):
    return render(request, 'frontend/notes.html')
    