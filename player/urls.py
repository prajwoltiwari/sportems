from django.urls import path
from . import views
from .views import TournamentAndWinnerListView, TeamTournamentAdditionView

urlpatterns = [
    path('', TournamentAndWinnerListView.as_view(), name='home'),
    path('tournament/team/', views.TeamTournamentAdditionView, name='team-tournament')
]