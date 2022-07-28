from django.contrib.auth.forms import UserCreationForm
from django import forms

from quiz.models import QuizPlayers, QuizRoom
from play.models import Quiz


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


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('quiz_Alist1', 'quiz_Alist2', 'quiz_Alist3', 'quiz_Alist4',
                  'quiz_answer', 'opencv_image', 'image')
        labels = {
            'quiz_alist1': '퀴즈 1문항',
            'quiz_alist2': '퀴즈 2문항',
            'quiz_alist3': '퀴즈 3문항',
            'quiz_alist4': '퀴즈 4문항',
            'quiz_answer': '퀴즈 정답',
            'opencv_image': '변형 이미지',
            'image': '원본 이미지',
        }
