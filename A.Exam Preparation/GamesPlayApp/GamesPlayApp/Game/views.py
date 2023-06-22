from django.shortcuts import render, redirect

from GamesPlayApp.Game.forms import GameForm, DeleteGameForm
from GamesPlayApp.Game.models import Game


def create_game(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(request, "create-game.html", {'form': form})


def game_details(request, id):
    game = Game.objects.get(id=id)
    return render(request, "details-game.html", {"game": game})


def edit_game(request, id):
    game = Game.objects.get(id=id)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(request, "edit-game.html", {"form": form, "id": id})


def delete_game(request, id):
    game = Game.objects.get(id=id)

    if request.method == 'POST':
        game.delete()
        return redirect("dashboard")

    form = DeleteGameForm(instance=game)
    return render(request, "delete-game.html", {"form": form, "id": id})

