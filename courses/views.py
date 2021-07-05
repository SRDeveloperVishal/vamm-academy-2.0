from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='account_login')
def courses_view(request):
    # links = YouTubeCoreses.objects.all()
    context = {
        # 'links': links,
    }
    return render(request, 'courses/index.html', context)
    