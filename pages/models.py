from django.db import models
from django.urls import reverse
from search.models import ArticleManager
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryPageModel(models.Model):
    name = models.CharField('Название категории', max_length=500)

    def __str__(self):
        return self.name

    def get_all(self):
        return Page.objects.filter(category=self)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Page(models.Model):
    """Модель страниц"""
    objects = ArticleManager()
    name = models.CharField("Заголовок", max_length=500)
    text = RichTextUploadingField('Тело статьи', blank=True, null=True, config_name='default')
    template = models.CharField("Шаблон", max_length=500, default="pages/index.html")
    category = models.ForeignKey(CategoryPageModel, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(
        "URL",
        max_length=500,
        unique=True,
        default='',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.slug:
            return reverse('page', kwargs={"page": self.slug})
        else:
            return reverse('page')

    def get_files(self):
        return FilesPage.objects.filter(parent_id=self.id)

    def get_accord(self):
        return AccordionModel.objects.filter(parent_id=self.id)

    def get_infograph(self):
        return InfographModel.objects.filter(parent_id=self.id)

    def get_bunner(self):
        return BunnerModel.objects.filter(parent_id=self.id)


class FilesPage(models.Model):
    """Файлы"""

    objects = ArticleManager()
    name = models.CharField('Название файла', max_length=500)
    file = models.FileField('Файл', upload_to='files/', max_length=500, null=True, blank=True)
    parent = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class AccordionModel(models.Model):
    name = models.CharField('Заголовок', max_length=1000)
    text = RichTextUploadingField('Текст', blank=True, null=True, config_name='default', )
    parent = models.ForeignKey(Page, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Аккордеон'
        verbose_name_plural = 'Аккордеоны'


class InfographModel(models.Model):
    picture = models.ImageField('Инфографика', upload_to="images/", blank=True, null=True)
    parent = models.ForeignKey(Page, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Инфографика'
        verbose_name_plural = 'Инфографика'


class BunnerModel(models.Model):
    text = text = RichTextUploadingField('Тело статьи', blank=True, null=True, config_name='default')
    parent = models.ForeignKey(Page, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
