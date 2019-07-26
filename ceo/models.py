from django.db import models


class CeoModel(models.Model):
    photo = models.ImageField('Фото', upload_to="images/", blank=True, null=True)
    name = models.CharField('Имя', max_length=500)
    position = models.CharField('Должность', max_length=500)
    phone = models.CharField('Телефон', max_length=100, blank=True, null=True)
    time = models.CharField('Время приема', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководителя'
        verbose_name_plural = 'Руководители'
