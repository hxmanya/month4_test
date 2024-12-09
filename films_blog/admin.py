from django.contrib import admin
from films_blog.models import FilmModel, Review

admin.site.register(FilmModel)
admin.site.register(Review)