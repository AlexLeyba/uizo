from django.db import models
from django.db.models import Q


class ArticleManager(models.Manager):
    """ Метод для реализации поиска по всему сайту"""

    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            try:
                or_lookup = (Q(name__icontains=query) | Q(text__icontains=query))
                qs = qs.filter(or_lookup)
            except:
                or_lookup = Q(name__icontains=query)
                qs = qs.filter(or_lookup)
        return qs
