from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import Tournament, Winner

# Create your views here.

class TournamentListView(ListView):
    model = Tournament
    template_name = 'player/home.html'
    # context_object_name = 'tournaments'
    # ordering = ['-start_time']
    # paginate_by = 5

    def get_context_data(self, **kwargs):
        ctx = super(TournamentListView, self).get_context_data(**kwargs)
        ctx['winners'] = Winner.objects.all()
        return ctx