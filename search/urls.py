from django.urls import path
from search.views import *

urlpatterns = [
    path('search/', SearchView.as_view(), name='search')
]
