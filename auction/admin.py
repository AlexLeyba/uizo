from django.contrib import admin
from auction.models import *


class FilesInstanceInlineAuction(admin.TabularInline):
    model = AuctionFiles


@admin.register(AuctionModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [FilesInstanceInlineAuction]
