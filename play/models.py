from django.db import models
import threading
import sys


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=200)
    quiz_Alist1 = models.CharField(max_length=200, null=True)
    quiz_Alist2 = models.CharField(max_length=200, null=True)
    quiz_Alist3 = models.CharField(max_length=200, null=True)
    quiz_Alist4 = models.CharField(max_length=200, null=True)

    quiz_answer = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/picture', blank=True, null=True)

    def __str__(self):
        return self.quiz_title


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_answer = models.IntegerField(default=0,null= True)
    player_score = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name



