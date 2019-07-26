from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from news.models import News
from .models import Page
from sliders.models import MainSliderModel, PartnersModel


class PageView(View):
    """Вывод страницы"""

    @staticmethod
    def get(request, page=None):
        if page is None:
            # главная
            one_page = get_object_or_404(Page, slug__isnull=True)
            last_four = News.objects.order_by('-id')[0:4]
            one_news = News.objects.all().last()
            top_slider = MainSliderModel.objects.all()
            bot_slider = PartnersModel.objects.all()
            context = {
                'page': one_page,
                'last_four': last_four,
                'one_news': one_news,
                'top_slider': top_slider,
                'bot_slider': bot_slider,
            }
        else:
            # все остальные страницы
            one_page = get_object_or_404(Page, slug=page)
            # files = Titles.objects.filter(parent_id=one_page.id)
            context = {'page': one_page}
        return render(request, one_page.template, context)
