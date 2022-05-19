from django.db import models

class Quiz(models.Model):
    quiz_title = models.CharField(max_length=200)
    quiz_Alist = models.CharField(max_length=200)
    quiz_answer = models.IntegerField(default=0)
    image = models.ImageField(blank=True)

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_score = models.IntegerField(default=0)


