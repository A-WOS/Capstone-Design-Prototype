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
            # return redirect('rooms')
            return redirect('rooms')
    else:
        form = PlayerForm()
    return render(request, 'quiz/signup_login.html', {'form': form})


def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        # print(form.fields[str('room_name')])
        # print(form.fields['room_name'])
        if form.is_valid():
            room = form.save(commit=False)
            room.room_host = request.user
            room.save()
            # print(f'dd {room.id}')
            # return render(request, 'quiz/in_room.html')
            return redirect('in_room', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'quiz/create_room.html', {'form': form})


# room.room_user = str()
# request.user = SimpleLazyObject
def in_room(request, room_id):
    room = get_object_or_404(QuizRoom, pk=room_id)
    print(f'room type : {room, type(room), room.id}')
    # room_details = QuizRoom.objects.get(room_name=room)
    # print(room_details)
    player = str(request.user)
    # room_details
    if player not in room.room_user:
        room.room_user += f'{player} '
    room.save()
    # print(f'room.room_??? types : {room.room_user, type(room.room_user), type(request.user)}')
    # print(f'request.GET.get("room_name") : {request.GET.get("room_name")}')
    context = {'room': room,
               'username': player}
    return render(request, 'quiz/in_room.html', context)


# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']
#     print(message)
#     print(f'send : {message, username, room_id}')
#     new_message = Message.objects.create(value=message, user=username, room=room_id)
#     new_message.save()
#     return HttpResponse('메시지 보내기 성공')
#
#
# def getMessages(request, room_id):
#     # messages = Message.objects.filter(room=room_id)
#     messages = Message.objects.get(room=room_id)
#     print(f'getMessages : {messages}')
#     return JsonResponse({"messages": list(messages.values())})


# def delete_user():
#     return
#
#
# def delete_room(request, room_id):
#     return
