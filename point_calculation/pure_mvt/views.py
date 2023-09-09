from django.shortcuts import render
from django.template import loader

def point(request):
    return render(request, "point.html")

def history(request):
    return render(request, "history.html")