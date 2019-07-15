from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Team, Tournament


class TeamRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length = 30, required = True, help_text = 'Please enter your Team-Name')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class TeamTournamentAdditionForm(forms.ModelForm):
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())
    identification = forms.ImageField(required = True)
    player_1 = forms.CharField(max_length = 30, required = False)
    player_2 = forms.CharField(max_length = 30, required = False)
    player_3 = forms.CharField(max_length = 30, required = False)
    player_4 = forms.CharField(max_length = 30, required = False)
    player_5 = forms.CharField(max_length = 30, required = False)
    player_6 = forms.CharField(max_length = 30, required = False)
    player_7 = forms.CharField(max_length = 30, required = False)
    player_8 = forms.CharField(max_length = 30, required = False)
    player_9 = forms.CharField(max_length = 30, required = False)
    player_10 = forms.CharField(max_length = 30, required = False)
    player_11 = forms.CharField(max_length = 30, required = False)
    player_12 = forms.CharField(max_length = 30, required = False)
    player_13 = forms.CharField(max_length = 30, required = False)
    player_14 = forms.CharField(max_length = 30, required = False)
    player_15 = forms.CharField(max_length = 30, required = False)
    class Meta:
        model = Team
        exclude = ['name', 'is_verified', 'created_date']

    def __init__(self, *args, **kwargs):
        super(TeamTournamentAdditionForm, self).__init__(*args, **kwargs)
        self.fields['tournament']=forms.ModelChoiceField(queryset=Tournament.objects.all())

