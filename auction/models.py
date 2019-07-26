from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AuctionModel(models.Model):
    text = RichTextUploadingField('Текст статьи', blank=True, null=True, config_name='default', )
    date = models.DateField('Дата', auto_now=True)

    def get_files(self):
        return AuctionFiles.objects.filter(parent_id=self.id)

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'


class AuctionFiles(models.Model):
    name = models.CharField('Название файла', max_length=1000, blank=True, null=True)
    file = models.FileField('Файл', upload_to='files/', null=True, blank=True)
    parent = models.ForeignKey(AuctionModel, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
