from django.shortcuts import render
from django.template import loader
from django.views.generic import View
from .forms import PointCalculationForm

def history(request):
    return render(request, "history.html")


class PureMvtCalcView(View):
    def get(self, request):
        f = PointCalculationForm()
        return render(request, "point.html", {'form': f} )

    def post(self, request):
        f = PointCalculationForm()
        return render(request, "point.html", {'form': f} )
