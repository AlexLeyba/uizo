from django.urls import path
from news.views import *

urlpatterns = [
    path('allnews/', AllNews.as_view(), name='allnews'),
    path('single/<int:pk>/', SingleNews.as_view(), name='single')
]
