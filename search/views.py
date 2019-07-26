from itertools import chain
from django.shortcuts import render
from django.views import View
from news.models import News, FilesNews
from pages.models import Page, FilesPage
from django.contrib import messages


class SearchView(View):
    """Поиск по всему сайту"""

    @staticmethod
    def post(request, *args, **kwargs):
        q = request.POST.get("q")
        context = {}
        final_set = []
        if q:
            query_sets = []
            query_sets.append(News.objects.search(query=q))
            query_sets.append(FilesPage.objects.search(query=q))
            query_sets.append(Page.objects.search(query=q))
            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.name, reverse=True)
            context = {
                'found': query_sets
            }
        if not final_set:
            messages.add_message(request, messages.ERROR,
                                 'Ничего не найдено, проверьте правильность вашего запроса.')
        return render(request, 'search/search.html', context)
