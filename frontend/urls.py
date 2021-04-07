from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home_url"),
    path('notes/', views.notes_view, name='notes_url'),
]
