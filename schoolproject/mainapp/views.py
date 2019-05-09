from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404, HttpResponseRedirect
# Create your views here.
def main(request):
    articles = Article.objects.all()[:3]
    print(articles)
    context = {'articles':articles}
    print(context)
    return render(request, 'mainapp/index.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def article(request, pk):
    article = get_object_or_404(Article,pk=pk)

    context = {'article':article}

    return render(request, 'mainapp/article.html', context)

def all_articles(request):
	all_news = Article.objects.all()
	context = {'all_news':all_news}
	return render(request, 'mainapp/all_articles.html', context)

def func():
	return 1




