from django.shortcuts import render
from django.http import HttpResponse

from food.models import Item
# Create your views here.

def index(request):

    item_list = Item.objects.all()
    return render(request, 'food/index.html', {
        'item_list': item_list
    })

def item(request):
    return HttpResponse('<h1>This is an Item.</h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'food/details.html', {
        'item': item
    })
