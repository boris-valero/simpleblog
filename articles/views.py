from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article

def list_articles(request):
    all_articles = Article.objects.filter(is_displayed=True, is_indexed=True)
    paginator = Paginator(all_articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.get_page(page)
    except PageNotAnInteger:
        articles = paginator.get_page(1)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)
    return render(request, 'articles/list.html', {'articles': articles})


