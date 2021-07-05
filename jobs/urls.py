from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_view, name="jobs"),
    
]
