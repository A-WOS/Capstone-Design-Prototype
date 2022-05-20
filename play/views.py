from django.shortcuts import render
from .models import Quiz


def index(request):
    quiz = Quiz.objects.all()
    return render(request, 'play/play_round.html', {'quiz': quiz})


def play_round_after(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    context = {'quiz': quiz}

    return render(request, 'play/play_round_after.html', context)
