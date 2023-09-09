from django.shortcuts import render
from django.template import loader

def order(request):
    return render(request, "order.html")

def history(request):
    return render(request, "history.html")