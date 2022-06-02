import django.contrib.auth.models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import QuizRoom, QuizPlayers
# from .models import QuizRoom
from .forms import PlayerForm, RoomForm


def index(request):
    room_list = QuizRoom.objects.all()
    context = {'room_list': room_list}
    return render(request, 'quiz/room_list.html', context)


def signup_login(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            auth = form.cleaned_data.get('auth')
            user = authenticate(username=username, password=raw_password, auth=auth)
            login(request, user)
            return redirect('rooms')
    else:
        form = PlayerForm()
    return render(request, 'quiz/signup_login.html', {'form': form})


# django.contrib.auth.models.User.set_unusable_password()


# def enter_room(request):
#     room_list = QuizRoom.objects.all()
#     context = {'room_list': room_list}
#     return render(request, 'quiz/room_list', context)

def create_room(request):
    # player = QuizPlayers.objects.get(username=QuizPlayers.username)
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('quiz:in_room')
    else:
        form = RoomForm()
    return render(request, 'quiz/create_room.html', {'form':form})


def in_room(request):
    return render(request, 'quiz/in_room.html')


def join_room(request):
    return render(request, 'quiz/join_room.html')