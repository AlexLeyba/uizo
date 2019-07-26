from search.models import ArticleManager
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    """Статья"""

    name = models.CharField('Заголовок', max_length=300)
    text = RichTextUploadingField('Текст статьи', blank=True, null=True, config_name='default', )
    date = models.DateField('Дата', auto_now_add=True)
    picture = models.ImageField('Картинка', upload_to="images/")
    objects = ArticleManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single', kwargs={'pk': self.id})

    def get_files(self):
        return FilesNews.objects.filter(parent_id=self.id)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class FilesNews(models.Model):
    """Файлы статьи"""

    photo = models.FileField('Картинка', upload_to='files/', max_length=500, null=True, blank=True)
    parent = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Картинку'
        verbose_name_plural = 'Картинки'
