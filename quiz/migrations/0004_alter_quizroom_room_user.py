# Generated by Django 4.0.3 on 2022-06-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quizroom_room_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizroom',
            name='room_user',
            field=models.CharField(max_length=1000),
        ),
    ]
