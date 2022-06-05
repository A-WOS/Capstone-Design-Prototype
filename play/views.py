from django.shortcuts import render
from .models import Quiz


def index(request):
    quiz = Quiz.objects.get(id=1)
    return render(request, 'play/play_round.html', {'quiz': quiz})


def play_round_after_fail(request):
    quiz = Quiz.objects.all()

    return render(request, 'play/play_round_after_fail.html',{'quiz': quiz})


def play_round_after_success(request):
    quiz = Quiz.objects.all()

    return render(request, 'play/play_round_after_success.html', {'quiz': quiz})

