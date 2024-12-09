from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('meals/', views.meal_products, name='meal_products'),
    path('drinks/', views.drink_products, name='drink_products'),
]