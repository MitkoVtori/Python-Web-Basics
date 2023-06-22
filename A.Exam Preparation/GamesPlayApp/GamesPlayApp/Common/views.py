from django.shortcuts import render

from GamesPlayApp.Game.models import Game


def home_page(request):
    return render(request, "home-page.html")


def dashboard(request):
    games = Game.objects.all()
    return render(request, "dashboard.html", {"games": games})

