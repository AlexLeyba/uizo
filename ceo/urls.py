from django.urls import path
from ceo.views import *

urlpatterns = [
    path('all-ceo/', CeoView.as_view(), name='ceo')

]
