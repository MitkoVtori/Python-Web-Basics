from django.shortcuts import render, redirect

from FruitipediaApp.Fruit.forms import FruitForm
from FruitipediaApp.Fruit.models import Fruit


def index(request):
    return render(request, "index.html")


def dashboard(request):
    fruits = Fruit.objects.all()
    return render(request, "dashboard.html", {"fruits": fruits})


def create_fruit(request):
    form = FruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(request, 'create-fruit.html', {"form": form})

