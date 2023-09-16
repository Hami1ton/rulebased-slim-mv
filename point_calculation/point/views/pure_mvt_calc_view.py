from django.shortcuts import render
from django.views.generic import View
from ..forms import PointCalculationForm
from ..models import SalesCampaign

def history(request):
     return render(request, "history.html")


class PureMvtCalcView(View):
    def get(self, request):
        f = PointCalculationForm()
        return render(request, "point.html", {"form": f} )

    def post(self, request):
        f = PointCalculationForm(request.POST)
        if f.is_valid():
            point = self.calculate(f)

            return render(request, "point.html", {
                "form": f,
                "point": point
                })
    
    def calculate(self, form_data):
        """
        calculate Points by the PointCalculationForm infomation  
        """
        card_rank = form_data.cleaned_data.get("card_rank")
        order_date = form_data.cleaned_data.get("order_date")
        shop = form_data.cleaned_data.get("shop")
        charge = form_data.cleaned_data.get("product").charge

        # decide point grant rate
        campaign = SalesCampaign.objects.filter(start_date__lte=order_date, end_date__gte=order_date)
        point_grant_rate = 1
        if card_rank == 1:
            point_grant_rate = 1
        elif card_rank == 2:
            point_grant_rate = 2
        elif card_rank == 3:
            point_grant_rate = 3

        if campaign.count() > 0:
            point_grant_rate = point_grant_rate * 1.5

        # decide point adding rate
        point_adding_rate = 1
        if shop.is_point_extra_service:
            point_adding_rate = 2

        return int((charge * point_grant_rate / 100) * point_adding_rate)
        
