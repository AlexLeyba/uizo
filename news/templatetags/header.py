from django import template
from pages.models import CategoryPageModel

register = template.Library()


@register.inclusion_tag('tags/header.html')
def menu():
    return {
        'category_about': CategoryPageModel.objects.filter(name='Об управлении'),
        'category_support': CategoryPageModel.objects.filter(name='Поддержка субъектов МСП'),
        'category_activity': CategoryPageModel.objects.filter(name='Деятельность'),
        'category_departments': CategoryPageModel.objects.filter(name='Отделы'),
        'category_auction': CategoryPageModel.objects.filter(name='Аукционы и конкурсы'),
        'category_contacts': CategoryPageModel.objects.filter(name='Контакты')}


@register.inclusion_tag('tags/menu_about.html')
def menu_about():
    return {
        'category_about': CategoryPageModel.objects.filter(name='Об управлении')}
