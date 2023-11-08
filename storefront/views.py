from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')

def say_item(request, item_id):
    """An item of the store"""
    return HttpResponse(f"Looking at {item_id}")

def say_search(request, term):
    """Search the store."""
    return HttpResponse(f"Searching for {term}")

def say_test(request, arg):
    """Search the store."""
    return HttpResponse(f"Testing for {arg}")
