# Generated by Django 4.0.3 on 2022-06-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('player_answer', models.IntegerField(default=0, null=True)),
                ('player_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_Alist1', models.CharField(max_length=200, null=True)),
                ('quiz_Alist2', models.CharField(max_length=200, null=True)),
                ('quiz_Alist3', models.CharField(max_length=200, null=True)),
                ('quiz_Alist4', models.CharField(max_length=200, null=True)),
                ('quiz_answer', models.IntegerField(default=0)),
                ('quiz_answer_name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/picture')),
            ],
        ),
    ]