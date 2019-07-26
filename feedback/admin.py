from django.contrib import admin
from feedback.models import FeedbackModel


@admin.register(FeedbackModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('author',)

