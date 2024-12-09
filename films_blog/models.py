from django.db import models

class FilmModel(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото фильма')
    title = models.CharField(max_length=100, verbose_name='укажите название фильма')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='укажите цену на фильм', default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Комедия')
    time_watch = models.TimeField(verbose_name='Укажите длительность фильма', blank=True)
    director = models.CharField(max_length=100, verbose_name='укажите режисера', default='Иван Иванов')
    trailer = models.URLField(verbose_name='укажите ссылку трейлера фильма', null=True)

#Если вы указываете новое поле то обязательно используйте атрибут null=True и занового проводите миграции
#Еще используете null True когда меняете поле
#После прописания всех полей проводим миграции 1ая команда python manage.py makemigrations 2ая python manage.py migrate
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.title


class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(verbose_name='напишите отзыв о фильме')
    stars = models.CharField(max_length=100, choices=STARS, verbose_name='поставьте оценку',
                             default='⭐')

    def __str__(self):
        return f'{self.film}:{self.stars}'
