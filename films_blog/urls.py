from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('emoji/', views.emoji, name='emoji'),
    path('photo/', views.image_proger_view, name='image_proger_view'),
]