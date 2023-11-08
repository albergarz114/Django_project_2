from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dating_shop(request):
    return HttpResponse("Welcome to the dating website! Where your future partner begins!!")