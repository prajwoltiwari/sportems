from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    FormView,
)
from .models import Tournament, Winner, Team
from .forms import TeamTournamentAdditionForm, TeamRegistrationForm

# Create your views here.

class TeamRegistrationView(FormView):
    form_class = TeamRegistrationForm
    template_name = 'player/team-register.html'

    def form_valid(self, form):
        form.save()
        teamname = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=teamname, password=raw_password)
        login(self.request, user)
        return redirect('home')



class TournamentAndWinnerListView(ListView):
    model = Tournament
    template_name = 'player/home.html'
    # ordering = ['-start_time']
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TournamentAndWinnerListView, self).get_context_data(**kwargs)
        context['winners'] = Winner.objects.all()
        return context



class TeamTournamentAdditionView(FormView):
       model = Team
       form_class = TeamTournamentAdditionForm
       template_name = 'player/team-tournament.html'

       def form_valid(self, form):
            success = form.save()
            success.name = self.request.user
            success.save()
            return redirect('home')
