from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    division = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class NBATeam(Team):
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_pct = models.FloatField()
    games_back = models.FloatField()
    home_record = models.CharField(max_length=20)
    away_record = models.CharField(max_length=20)
    div_record = models.CharField(max_length=20)
    conf_record = models.CharField(max_length=20)
    ppg = models.FloatField()
    opp_ppg = models.FloatField()
    diff = models.FloatField()
    streak = models.CharField(max_length=10)
    last_10 = models.CharField(max_length=10)
    playoff_status = models.CharField(max_length=1)

class MLBTeam(Team):
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_pct = models.FloatField()
    gb = models.CharField(max_length=10, null=True, blank=True)
    home_record = models.CharField(max_length=20)
    away_record = models.CharField(max_length=20)
    runs_scored = models.IntegerField()
    runs_against = models.IntegerField()
    run_diff = models.IntegerField()
    streak = models.CharField(max_length=10)
    last_10 = models.CharField(max_length=10)


class NFLTeam(Team):
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    win_pct = models.FloatField()
    home_record = models.CharField(max_length=20)
    away_record = models.CharField(max_length=20)
    div_record = models.CharField(max_length=20)
    conf_record = models.CharField(max_length=20)
    points_for = models.IntegerField()
    points_against = models.IntegerField()
    point_diff = models.IntegerField()
    streak = models.CharField(max_length=10)
    playoff_status = models.CharField(max_length=1)

class LeagueStandings(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField()
    league = models.CharField(max_length=50)
    win_pct = models.FloatField()
    games_back = models.FloatField(null=True, blank=True)
    streak = models.CharField(max_length=10)
    last_10 = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.team.name} - Position: {self.position}, League: {self.league}"
