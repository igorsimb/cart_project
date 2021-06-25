from django.shortcuts import render, redirect

from .models import Topping

def index(request):
    topping_list = Topping.objects.all()
    context = {'topping_list': topping_list}
    return render(request, 'cart/index.html', context)


def toppingAdd(request, topping_id):
    topping = Topping.objects.get(pk=topping_id)
    topping.is_added = True

    #TODO: create total for all topping prices and make it show in Template
    print(f'TOPPING PRICE = {topping.price}')

    topping.save()

    return redirect('index')


def toppingRemove(request, topping_id):
    topping = Topping.objects.get(pk=topping_id)
    topping.is_added = False

    topping.save()
    return redirect('index')
