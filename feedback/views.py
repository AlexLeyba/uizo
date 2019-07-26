from django.shortcuts import redirect
from django.views.generic import CreateView
from feedback.forms import FeedbackForm
from feedback.models import FeedbackModel
from django.contrib import messages


class FeedbackView(CreateView):
    model = FeedbackModel
    template_name = 'feedback/form.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO,
                             'Ваше обращение успешно зарегистрировано.')
        return redirect('/feedback/form/')
