from django.shortcuts import render
from . import models


def index(request):
    return render(request, "index.html")


def basics(request):
    lectures_list = models.Lecture.objects.all().order_by("Index")
    context = {"lectures_list": lectures_list}
    return render(request, "basics.html", context)

