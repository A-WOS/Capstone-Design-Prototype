from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import QuizRoom
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# import re


def CreateRoomView(request):
    return render(request, 'room/create_room.html')


# def QuizView(request, room_name):
#     if not re.match(r'^[\w-]*$', room_name):
#         return render(request, 'quiz/error.html')
#     return render(request, 'quiz/quiz.html')


@csrf_exempt
def roomExist(request, room_name):
    print(room_name)

    return JsonResponse({
        "room_exist": QuizRoom.objects.filter(room_name=room_name).exists()
    })

# from django.http import HttpResponse
# from django.shortcuts import render
# # from .models import Room
#
#
# # def index(request):
# #     room_list = Room.objects.order_by('-room_id')
# #     context = {'room_list': room_list}
# #     return render(request, 'room/room_list.html', context)
#
# # from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("quiz 메인페이지")
