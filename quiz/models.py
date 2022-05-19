from django.db import models


class QuizRoom(models.Model):
    room_name = models.CharField(max_length=100)
    room_pw = models.IntegerField()
    room_invited_code = models.CharField(max_length=50)
    room_play_round = models.IntegerField()
    room_round_limit_time = models.IntegerField()

    def __str__(self):
        return self.room_name


class QuizPlayers(models.Model):
    username = models.CharField(max_length=100)
    room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.username