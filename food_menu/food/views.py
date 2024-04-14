from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    print(item_list)
    return HttpResponse(item_list)

def item(request):
    return HttpResponse("<h1>This is my new view</h1>")