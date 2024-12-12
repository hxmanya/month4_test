from django.db import models
from films_blog.models import FilmModel

class TodoModel(models.Model):
    CHECKING = (
        ('✅', '✅'),
        ('❌', '❌')
    )
    title = models.CharField(max_length=100)
    description = models.TextField(default='Начну с .........')
    choice_check = models.CharField(max_length=10, choices=CHECKING)
    film_by = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='buy_film', null=True)

    def __str__(self):
        return self.title

