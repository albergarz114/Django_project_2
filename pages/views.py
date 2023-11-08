from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_book(request):
    return HttpResponse('Let us read and be calm!')

def shop_item(request, item_id):
    """An item of the shop."""
    return HttpResponse(f"Looking at {item_id}")

def shop_search(request, term):
    """Search the shop."""
    return HttpResponse(f"Searching for {term}")

def shop_test(request, arg):
    """Search the shop."""
    return HttpResponse(f"Testing for {arg}")