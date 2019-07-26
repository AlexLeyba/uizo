from django.contrib import admin
from .models import Page, FilesPage, CategoryPageModel, AccordionModel, InfographModel, BunnerModel


class InstanceInlineInfo(admin.TabularInline):
    model = InfographModel


class FilesInstanceInlinePage(admin.TabularInline):
    model = FilesPage


class AccordInstanceInlinePage(admin.TabularInline):
    model = AccordionModel


class BunnerInstanceInlinePage(admin.TabularInline):
    model = BunnerModel


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Админ страниц"""
    list_display = ("name", "id")
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FilesInstanceInlinePage, AccordInstanceInlinePage, InstanceInlineInfo, BunnerInstanceInlinePage]


@admin.register(CategoryPageModel)
class PageAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name",)
