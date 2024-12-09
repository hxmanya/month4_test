from django.shortcuts import render
from . import models

#все продукты
def all_products(request):
    if request.method == "GET":
        products = models.Product.objects.all().order_by('-id')
        context = {'products': products}
        return render(
            request,
            template_name='tags/all_products.html',
            context=context
        )
#все напитки
def drink_products(request):
    if request.method == "GET":
        products_drink = models.Product.objects.filter(tags__name='Напитки').order_by('-id')
        context = {'products_drink': products_drink}
        return render(
            request,
            template_name='tags/drink_products.html',
            context=context
        )

#вся еда
def meal_products(request):
    if request.method == "GET":
        products_meal = models.Product.objects.filter(tags__name='Еда').order_by('-id')
        context = {'products_meal': products_meal}
        return render(
            request,
            template_name='tags/meal_products.html',
            context=context
        )