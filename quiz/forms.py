from django.contrib.auth.forms import UserCreationForm
from django import forms

from quiz.models import QuizPlayers, QuizRoom


class PlayerForm(UserCreationForm):
    auth = forms.IntegerField(label='권한')

    class Meta:
        model = QuizPlayers
        fields = ('username', 'auth')
        labels = {'username': '유저명', 'auth': '권한'}


class RoomForm(forms.ModelForm):
    class Meta:
        model = QuizRoom
        # fields = ('room_name', 'room_pw', 'room_invited_code', 'room_play_round', 'room_round_limit_time')
        # 'room_pw': '방 비밀번호',
        # 'room_invited_code': '초대코드',
        fields = ('room_name', 'room_play_round', 'room_round_limit_time')
        labels = {
            'room_name': '방제목',
            'room_play_round': '라운드',
            'room_round_limit_time': '제한시간',
        }
