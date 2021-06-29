from django.shortcuts import render, redirect
from django.db.models import Sum, Min, Max, Avg

from .models import Topping

def index(request):
    topping_list = Topping.objects.all()
    # show price Sum of toppings that were added to Your Cart
    topping_price = Topping.objects.filter(is_added=True).aggregate(total_price=Sum('price'))
    context = {'topping_list': topping_list, 'topping_price': topping_price}
    return render(request, 'cart/index.html', context)


def toppingAdd(request, topping_id):
    topping = Topping.objects.get(pk=topping_id)
    # topping_price = Topping.objects.get(pk=topping_id).aggregate(total_price=Sum('price'))

    topping.is_added = True


    print(f'TOPPING PRICE = {topping.price}')

    topping.save()
    # topping_price.save()

    return redirect('index')


def toppingRemove(request, topping_id):
    topping = Topping.objects.get(pk=topping_id)
    topping.is_added = False

    topping.save()
    return redirect('index')
