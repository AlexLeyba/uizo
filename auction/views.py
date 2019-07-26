from django.shortcuts import render
from django.views import View
from auction.models import AuctionModel


class Auction(View):
    def get(self, request):
        auction = AuctionModel.objects.all()
        return render(request, 'auction/auction.html', {'auction': auction})
