from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# получение id и получение полной информации о фильме
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.FilmModel, id=id)
        context = {
            'film_id': film_id,
        }
        return render(request, template_name='show_detail.html', context=context)


# не полная информация
def film_list_view(request):
    if request.method == "GET":
        # query запрос что мы хотим видеть на html странице
        film_list = models.FilmModel.objects.all().order_by('-id')
        # context_object_name = нужен для передачи данных на html шаблон в виде ключа
        context = {
            'film_list': film_list,
        }
        return render(request, template_name='show.html', context=context)


def about(request):
    if request.method == "GET":
        return HttpResponse('Привет это мой первый проект на django')


def emoji(request):
    if request.method == "GET":
        return HttpResponse('😀 🥲 🧐 😎 🥸 🤫 🫢')


def image_proger_view(request):
    if request.method == "GET":
        return HttpResponse(
            '<img src="https://blog.tutortop.ru/wp-content/uploads/2023/04/speczialist-v-it-sfere.jpg">')
