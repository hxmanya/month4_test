from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list_view, name='films'),
    path('film_detail/<int:id>/', views.film_detail_view, name='film_detail'),
    path('about/', views.about, name='about'),
    path('emoji/', views.emoji, name='emoji'),
    path('photo/', views.image_proger_view, name='image_proger_view'),
]