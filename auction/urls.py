from django.urls import path
from auction.views import *

urlpatterns = [
    path('all-auction/', Auction.as_view(), name='auction')

]
