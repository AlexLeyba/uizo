from django.db import models


class MainSliderModel(models.Model):
    """Основной слайдер"""

    picture = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)
    url = models.CharField('url', max_length=500, blank=True, null=True)
    name = models.CharField('Заголовок', max_length=1000, blank=True, null=True)
    text = models.TextField('Текст', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Верхний слайдер'
        verbose_name_plural = 'Верхние слайдеры'


class PartnersModel(models.Model):
    """Слайдер с партнерами"""

    picture = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)
    url = models.CharField('url', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Слайдер партнеры'
        verbose_name_plural = 'Слайдеры партнеры'
