from django.contrib.auth.models import AbstractUser, User
from django.db import models


class QuizRoom(models.Model):
    room_name = models.CharField(max_length=100)
    # room_pw = models.IntegerField()
    # room_invited_code = models.CharField(max_length=50)
    room_play_round = models.IntegerField()
    room_round_limit_time = models.IntegerField()
    room_host = models.CharField(max_length=30)
    room_user = models.CharField(max_length=1000)

    def __str__(self):
        return self.room_name


class QuizPlayers(User):
    auth = models.IntegerField(default=0)
    room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE, null=True)
    player_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Message(models.Model):
    value = models.CharField(max_length=10000)
    user = models.CharField(max_length=100)
    room = models.IntegerField(default=0)
    # room = models.CharField(max_length=1000)
    # room = models.ForeignKey(QuizRoom, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.value
