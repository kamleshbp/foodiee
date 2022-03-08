from django.shortcuts import render, redirect
from django.http import HttpResponse

from food.models import Item
from .forms import ItemForm

from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

# Create your views here.

def index(request):

    item_list = Item.objects.all()
    return render(request, 'food/index.html', {
        'item_list': item_list
    })

# class based view

class IndexClassView(ListView):

    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


# def item(request):
#     return HttpResponse('<h1>This is an Item.</h1>')

@login_required
def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'food/details.html', {
        'item': item
    })

@login_required
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {
        'form': form
    })

@login_required
def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {
        'form': form
    })

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {
        'item': item
    })
