from django import forms
from feedback.models import FeedbackModel


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ('author', 'email', 'phone', 'text', 'check', 'check2')
        labels = {'author': '',
                  'email': '',
                  'phone': '', 'text': '', 'check': '', 'check2': ''}
