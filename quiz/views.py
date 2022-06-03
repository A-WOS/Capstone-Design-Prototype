import django.contrib.auth.models
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import QuizRoom, QuizPlayers, Message
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


def create_room(request):
    # player = QuizPlayers.objects.get(username=QuizPlayers.username)
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.room_host = request.user
            room.save()
            # checkview(room.room_name, request.user)
            return render(request, 'quiz/in_room.html')
    else:
        form = RoomForm()
    return render(request, 'quiz/create_room.html', {'form': form})


def in_room(request, room_id):
    room = get_object_or_404(QuizRoom, pk=room_id)
    # if request.user not in room.room_user:
    room.room_user += f'{request.user} '
    # set(room.room_user)
    # checkview(room.room_name, request.user)
    room.save()
    print(room.room_user, type(room.room_user), type(request.user))
    context = {'room': room}
    return render(request, 'quiz/in_room.html', context)


# chat
# def checkview(r, u):
#     # room = request.POST['room_name']
#     # username = request.POST['username']
#     # username = request.user
#     room = r
#     username = u
#
#     if QuizRoom.objects.filter(name=room).exists():
#         return redirect('/' + room + '/?username=' + username)
#     # else:
#     #     new_room = QuizRoom.objects.create(name=room)
#     #     new_room.save()
#     #     return redirect('/' + room + '/?username=' + username)


# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']
#
#     new_message = Message.objects.create(value=message, user=username, room=room_id)
#     new_message.save()
#     return HttpResponse('Message sent successfully')
#
#
# def getMessages(request, room_id):
#     room = QuizRoom.objects.get(name=room_id)
#
#     messages = Message.objects.filter(room=room.id)
#     return JsonResponse({"messages": list(messages.values())})

# def room(request):
#     username = request.user
#     # room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#     })
