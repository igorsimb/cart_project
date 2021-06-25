from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topping-add/<topping_id>/', views.toppingAdd, name='topping_add'),
    path('topping-remove/<topping_id>/', views.toppingRemove, name='topping_remove'),
]