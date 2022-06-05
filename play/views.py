from django.shortcuts import render
from .models import Quiz
from django.views.decorators.csrf import csrf_exempt


def index(request):
    quiz = Quiz.objects.get(id=1)
    return render(request, 'play/play_round.html', {'quiz': quiz})



def play_round_after(request):
    round = request.POST['round']
    quiz = Quiz.objects.get(id=round)

    return render(request, 'play/play_round_after_success.html', {'quiz' : quiz})

def play_round(request):
    round = request.POST['round']

    quiz = Quiz.objects.get(id=int(round)+1)

    return render(request, 'play/play_round.html',{'quiz': quiz})