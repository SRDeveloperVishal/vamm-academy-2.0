from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import * 

# Create your views here.
@login_required(login_url='account_login')
def courses_view(request):
    courses = YouTubeCourses.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)
    