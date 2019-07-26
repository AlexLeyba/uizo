from django.shortcuts import render
from django.views import View
from ceo.models import CeoModel


class CeoView(View):
    def get(self, request):
        ceo = CeoModel.objects.all()
        context = {'ceo': ceo}
        return render(request, 'management/ceo.html', context)
