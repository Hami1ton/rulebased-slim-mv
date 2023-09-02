from django.shortcuts import render
from django.template import loader

def index(request):
    template = loader.get_template("sample.html")
    context = {
        "latest_question_list": "",
    }
    return render(request, "sample.html", context)