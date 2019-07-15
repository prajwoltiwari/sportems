from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TournamentAndWinnerListView, TeamTournamentAdditionView, TeamRegistrationView

urlpatterns = [
    path('', TournamentAndWinnerListView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='player/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('team/register/', TeamRegistrationView.as_view(), name='team-register'),
    path('tournament/team/', TeamTournamentAdditionView.as_view(), name='team-tournament'),
]