# Generated by Django 4.0.3 on 2022-06-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizroom',
            name='room_user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
