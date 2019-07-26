from django.contrib import admin
from sliders.models import MainSliderModel, PartnersModel


@admin.register(MainSliderModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(PartnersModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',)
