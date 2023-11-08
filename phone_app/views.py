from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def apple_phone(request):
    return HttpResponse('Hello this is me. How can I help you?')