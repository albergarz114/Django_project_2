from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tennis_shop(request):
    return HttpResponse('Welcome to my tennis shop! We have tennis shoes, tennis rackets, etc.')
