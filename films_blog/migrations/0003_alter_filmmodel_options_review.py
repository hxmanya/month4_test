# Generated by Django 5.1.3 on 2024-12-09 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_blog', '0002_filmmodel_trailer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmmodel',
            options={'verbose_name': 'фильм', 'verbose_name_plural': 'фильмы'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('text_review', models.TextField(verbose_name='напишите отзыв о фильме')),
                ('stars', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], default='⭐', max_length=100, verbose_name='поставьте оценку')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='films_blog.filmmodel')),
            ],
        ),
    ]
