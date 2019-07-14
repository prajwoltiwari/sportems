from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Team, Tournament


class TeamRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# class TeamRegistrationForm(forms.ModelForm):
#     tournament_ = forms.CharField()

#     class Meta:
#         model = Team

#     def save(self, commit=True):
#         tournament, created = Team.objects.get_or_create(
#             tournament=self.cleaned_data['tournament_'],
#         )
#         self.cleaned_data['tournament_'] = tournament.id
#         return super(TeamRegistrationForm, self).save(commit)



class TeamTournamentAdditionForm(forms.ModelForm):
    identification = forms.ImageField(required = True)
    created_date = forms.DateTimeField(required = True)
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
    player_11= forms.CharField(max_length = 30, required = False)
    player_12= forms.CharField(max_length = 30, required = False)
    player_13= forms.CharField(max_length = 30, required = False)
    player_14= forms.CharField(max_length = 30, required = False)
    player_15= forms.CharField(max_length = 30, required = False)
    class Meta:
        model = Team
        exclude = ['name', 'is_verified']

    def __init__(self, *args, **kwargs):
        super(TeamTournamentAdditionForm, self).__init__(*args, **kwargs)
        self.fields['tournament']=forms.ModelChoiceField(queryset=Tournament.objects.all())

