from django.shortcuts import render,redirect
from .models import Article
import time

# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time= time.ctime(time.time()),
        )
        return redirect('detail', article_pk=new_article.pk)
    
    return render(request, 'new.html')

def index(request):
    drama_num= Article.objects.filter(category ='drama').count()
    movie_num= Article.objects.filter(category ='movie').count()
    programming_num= Article.objects.filter(category ='programming').count()
    article = Article.objects.all()
    return render(request, 'index.html', {'article': article,'drama_num': drama_num,'movie_num': movie_num,'programming_num': programming_num})


def detail(request, article_pk):
    article=Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article':article})

def drama(request):
    article_drama = Article.objects.filter(category = 'drama')
    return render(request, 'drama.html', {'articles': article_drama})

def movie(request):
    article_movie = Article.objects.filter(category = 'movie')
    return render(request, 'movie.html', {'articles':article_movie})

def programming(request):
    article_programming = Article.objects.filter(category = 'programming')
    return render(request, 'programming.html', {'articles': article_programming})


    
