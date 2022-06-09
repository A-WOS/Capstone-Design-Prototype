from django.shortcuts import render

from quiz.models import QuizPlayers
from .models import Quiz, Player
from django.views.decorators.csrf import csrf_exempt


def index(request):
    quiz = Quiz.objects.get(id=1)
    # player = Player.objects.get(id=request.user.id)
    player = QuizPlayers.objects.get(id=request.user.id)
    print(player)
    player.player_score = 0
    player.save()
    return render(request, 'play/play_round.html', {'quiz': quiz})


def play_round_after(request):
    round = request.POST['round']
    U_ans = request.POST['U_ans']
    print(type(U_ans))
    quiz = Quiz.objects.get(id=round)
    print(type(quiz.quiz_answer))
    player = QuizPlayers.objects.get(id=request.user.id)
    # player = Player.objects.get(id=request.user.id)
    if (quiz.quiz_answer == int(U_ans)):
        player.player_score += 10
        player.save()

    return render(request, 'play/play_round_after.html', {'quiz': quiz, 'U_ans': int(U_ans), 'player': player})


def play_round(request):
    round = request.POST['round']

    quiz = Quiz.objects.get(id=int(round) + 1)

    return render(request, 'play/play_round.html', {'quiz': quiz})


def play_result(request):
    # player_list = Player.objects.order_by('id')
    player = QuizPlayers.objects.get(id=request.user.id)
    context = {'player': player}

    return render(request, 'play/play_result.html', context)
