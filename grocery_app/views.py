from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def grocery_shop(request):
    return HttpResponse('Welcome to my grocery shop! Mi casa es su casa!!')