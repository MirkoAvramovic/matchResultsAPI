from django.db import models

class Match(models.Model):
    home = models.CharField(max_length=20)
    away = models.CharField(max_length=20)
    home_scored = models.IntegerField(default=0)
    away_scored = models.IntegerField(default=0)
    match_status = models.CharField(max_length=30)

    def __str__(self):
        return self.home + ' - ' + self.away + '(' + str(self.home_scored) + ' : ' + str(self.away_scored) + ')'