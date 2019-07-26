from django.urls import path
from menu.views import *

urlpatterns = [
    path('about/', About.as_view(), name='about')
]
