# Generated by Django 4.0.3 on 2022-05-19 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('room_pw', models.IntegerField()),
                ('room_invited_code', models.CharField(max_length=50)),
                ('room_play_round', models.IntegerField()),
                ('room_round_limit_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuizPlayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizroom')),
            ],
        ),
    ]
