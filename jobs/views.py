from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import * 

# Create your views here.
@login_required(login_url='account_login')
def jobs_view(request):
    job = jobs.objects.all()
    context = {
        'jobs': job,
    }
    return render(request, 'jobs/index.html', context)
    
