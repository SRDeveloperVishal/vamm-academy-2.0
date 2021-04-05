from django.shortcuts import render
from .models import *

# Create your views here.
# Create your views here.
def home_view(request):
    links = YouTubeCoreses.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'frontend/index.html', context)