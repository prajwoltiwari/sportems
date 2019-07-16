from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tournament(models.Model):
    LEVEL_CHOICES = (
        ('regional', 'Regional'),
        ('district', 'District'),
    )
    TOURNAMENT_TYPE_CHOICES = (
        ('cricket', 'Cricket'),
        ('football', 'Football'),
    )
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    title = models.CharField(max_length=100, blank = True, null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=100)
    tournament_type = models.CharField(choices=TOURNAMENT_TYPE_CHOICES, max_length=100)
    venue = models.CharField(max_length=100, blank = True, null=True)
    gender = models.CharField(choices=GENDER, max_length=100)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to='tournament_images')


    def __str__(self):
        return f'{self.title}'


class Team(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    identification = models.ImageField(null=True, upload_to='identification_card')
    created_date = models.DateTimeField(default=timezone.now)
    player_1 = models.CharField(max_length=100, blank = True, null=True)
    player_2 = models.CharField(max_length=100, blank = True, null=True)
    player_3 = models.CharField(max_length=100, blank = True, null=True)
    player_4 = models.CharField(max_length=100, blank = True, null=True)
    player_5 = models.CharField(max_length=100, blank = True, null=True)
    player_6 = models.CharField(max_length=100, blank = True, null=True)
    player_7 = models.CharField(max_length=100, blank = True, null=True)
    player_8 = models.CharField(max_length=100, blank = True, null=True)
    player_9 = models.CharField(max_length=100, blank = True, null=True)
    player_10 = models.CharField(max_length=100, blank = True, null=True)
    player_11 = models.CharField(max_length=100, blank = True, null=True)
    player_12 = models.CharField(max_length=100, blank = True, null=True)
    player_13 = models.CharField(max_length=100, blank = True, null=True)
    player_14 = models.CharField(max_length=100, blank = True, null=True)
    player_15 = models.CharField(max_length=100, blank = True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank = True, null=True)
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name= 'first_team')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name= 'second_team')
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} match'


class Winner(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True)
    gold_medalist = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name= 'winner')
    silver_medalist = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name= 'first_runner_up')
    bronze_medalist = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True, related_name= 'second_runner_up')

    def __str__(self):
        return f'{self.tournament} winner list'