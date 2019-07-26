from django.shortcuts import render
from django.views import View
from news.models import *


class AllNews(View):
    """Вывод всех новостей"""

    @staticmethod
    def get(request):
        news = News.objects.order_by('id')[::-1]
        context = {
            'news': news
        }
        return render(request, 'news/all-news.html', context)


class SingleNews(View):
    """Вывод полной статьи"""

    @staticmethod
    def get(request, pk):
        single = News.objects.get(id=pk)
        last_eight = News.objects.order_by('-id')[0:8]
        context = {
            'single': single,
            'last_eight': last_eight
        }
        return render(request, 'news/news-detail.html', context)
