from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def play(request):
    return HttpResponse('Which sport is your favorite?')

def quit(request):
    return HttpResponse('Do you want to quit?')