from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(verbose_name='Название новости', max_length=64)
    textOfArtic = models.TextField(verbose_name='Текст новости', blank=True)
    decription = models.TextField(verbose_name='Описание новости')
    image = models.ImageField(verbose_name='Фото в статье', blank=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
