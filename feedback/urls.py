from django.urls import path
from feedback.views import *

urlpatterns = [
    path('form/', FeedbackView.as_view(), name='feedback')
]
