app_name='mainapp'

from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp
urlpatterns = [
    path('read/<int:pk>/', mainapp.article, name='article_read'),
    path('news/', mainapp.all_articles, name='all_news'),
    path('contact/', mainapp.contact, name='contact'),
]