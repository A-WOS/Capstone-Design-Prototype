from django.db import models
import threading
import sys

from quiz.models import QuizPlayers


class Quiz(models.Model):
    quiz_Alist1 = models.CharField(max_length=200, null=True)
    quiz_Alist2 = models.CharField(max_length=200, null=True)
    quiz_Alist3 = models.CharField(max_length=200, null=True)
    quiz_Alist4 = models.CharField(max_length=200, null=True)

    quiz_answer = models.IntegerField(default=0)
    quiz_answer_name = models.CharField(max_length=200, null=True)

    # 추가된 opencv img 칼럼
    opencv_image = models.ImageField(upload_to='static/picture', blank=True, null=True)
    image = models.ImageField(upload_to='static/picture', blank=True, null=True)

    def __int__(self):
        return self.quiz_answer


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    # player_name = QuizPlayers.username
    player_answer = models.IntegerField(default=0,null= True)
    player_score = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name



