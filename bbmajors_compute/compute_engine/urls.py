from django.urls import path
from . import views


urlpatterns = [
    path('players/', views.players, name='players'),
    path('teams/', views.teams, name='teams'),
    path('ajax/calculate_teams', views.calculate_teams, name='calculate_teams')
]