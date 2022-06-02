from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django_mysql.models import ListCharField


class QuizRoom(models.Model):
    room_name = models.CharField(max_length=100)
    room_pw = models.IntegerField()
    room_invited_code = models.CharField(max_length=50)
    room_play_round = models.IntegerField()
    room_round_limit_time = models.IntegerField()
    room_host = models.CharField(max_length=30)
    room_user = models.CharField(max_length=1000)
    # room_user = ListCharField(
    #     base_field=models.CharField(max_length=20),
    #     size=10,
    #     max_length=(20*11),
    # )

    def __str__(self):
        return self.room_name


class QuizPlayers(User):
    # user = models.OneToOneField(User)
    auth = models.IntegerField(default=0)
    room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username



# class QuizPlayers(models.Model):
#     username = models.CharField(max_length=100)
#     room = models.ForeignKey(QuizRoom, on_delete=models.CASCADE)
#