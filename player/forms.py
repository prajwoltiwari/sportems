from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Team


class UserRegistrationForm(UserCreationForm):
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

