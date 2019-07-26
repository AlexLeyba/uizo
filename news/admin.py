from django.contrib import admin
from news.models import *


class FilesInstanceInlineNews(admin.TabularInline):
    model = FilesNews


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [FilesInstanceInlineNews]
