from django.db import models


class FeedbackModel(models.Model):
    """Форма обращения"""

    author = models.CharField('ФИО', max_length=500)
    email = models.EmailField('email для ответа', blank=True, null=True)
    phone = models.CharField('телефон', max_length=50)
    text = models.TextField('текст обращения')
    check = models.BooleanField('согласие', default=True)
    check2 = models.BooleanField('согласие', default=True)
    ready = models.BooleanField('обработано', default=False)

    class Meta:
        verbose_name = 'Обращения'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.author
