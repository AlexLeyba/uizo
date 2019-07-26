from django.contrib import admin
from ceo.models import CeoModel


@admin.register(CeoModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name',)
