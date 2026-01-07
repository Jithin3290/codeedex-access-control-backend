from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class TeamMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
