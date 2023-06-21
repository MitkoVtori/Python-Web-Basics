from django.shortcuts import render, redirect

from MyMusicApp.MyMusicApp.Album.models import Album
from MyMusicApp.MyMusicApp.Profile.models import Profile


def profile_details(request):
    return render(request, "profile-details.html", {"albums": Album.objects.all()})


def delete_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()

        return redirect('home')

    return render(request, 'profile-delete.html')