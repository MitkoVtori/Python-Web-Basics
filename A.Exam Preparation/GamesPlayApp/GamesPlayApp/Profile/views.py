from django.shortcuts import render, redirect

from GamesPlayApp.Game.models import Game
from GamesPlayApp.Profile.forms import ProfileForm, EditProfileForm
from GamesPlayApp.Profile.models import Profile


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "create-profile.html", {"form": form})


def average_games_rating():
    rating = []
    for game in Game.objects.all():
        rating.append(game.rating)
    return sum(rating) / len(rating)


def profile_details(request):
    return render(request, "details-profile.html", {"games": Game.objects.all(), "rating": average_games_rating()})


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("profile")

    return render(request, "edit-profile.html", {"form": form})


def delete_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    if request.method == "POST":
        profile.delete()
        games.delete()
        return redirect("home")

    return render(request, "delete-profile.html")

