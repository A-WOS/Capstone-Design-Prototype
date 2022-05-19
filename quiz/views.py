from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("quiz 메인페이지")
