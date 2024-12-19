from django.urls import path
from . import views

urlpatterns = [
    path('rezka_film_list/', views.RezkaListView.as_view(), name='rezka_list'),
    path('form_parser_rezka/', views.RezkaFormView.as_view()),
]