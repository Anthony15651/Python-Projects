from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Anthony", "Cella", "Carrie", "Hazel", "Barney"]
    context = {
        'names': names,
    }
    return render(request, "home.html", context)
