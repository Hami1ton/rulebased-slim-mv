from django.shortcuts import render
from django.template import loader

from .forms import PointCalculationForm

def point(request):
    f = PointCalculationForm()
    return render(request, "point.html", {'form': f} )

def history(request):
    return render(request, "history.html")