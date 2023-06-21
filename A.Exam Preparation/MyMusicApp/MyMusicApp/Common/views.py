from django.shortcuts import render, redirect

from MyMusicApp.MyMusicApp.Album.models import Album
from MyMusicApp.MyMusicApp.Profile.forms import ProfileForm
from MyMusicApp.MyMusicApp.Profile.models import Profile


def index(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")

        return render(request, "home-no-profile.html", {"form": form})

    else:
        albums = Album.objects.all()
        return render(request, "home-with-profile.html", {"albums": albums})

