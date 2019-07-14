from django.shortcuts import render, render_to_response, redirect
from django.views.generic import (
    ListView,
)
from .models import Tournament, Winner
from .forms import TeamTournamentAdditionForm, TeamRegistrationForm

# Create your views here.

class TournamentAndWinnerListView(ListView):
    model = Tournament
    template_name = 'player/home.html'
    # context_object_name = 'tournaments'
    # ordering = ['-start_time']
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TournamentAndWinnerListView, self).get_context_data(**kwargs)
        context['winners'] = Winner.objects.all()
        return context


def TeamTournamentAdditionView(request):
    if request.method=='POST':
        form=TeamTournamentAdditionForm(request.POST)
        print(form)
        if form.is_valid():
            tournament_ = form.cleaned_data.get('tournament')
            team_tournament = Tournament(tournament=tournament_)
            team_tournament.save()
            team = form.save(commit=False)
            team.tournament = team_tournament
            team.save()
            return redirect('home')
    else:
        form=TeamTournamentAdditionForm()

    context = { 'form' : form }

    return render(request, 'player/team-tournament.html', context)
