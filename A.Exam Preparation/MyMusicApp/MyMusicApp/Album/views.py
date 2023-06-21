from django.shortcuts import render, redirect

from MyMusicApp.MyMusicApp.Album.forms import AlbumForm, DeleteAlbumForm
from MyMusicApp.MyMusicApp.Album.models import Album


def add_album(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "add-album.html", {"form": form})


def album_details(request, id):
    album = Album.objects.get(id=id)
    album.price = f'{album.price:.2f}'
    return render(request, "album-details.html", {"album": album})


def edit_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "edit-album.html", {"form": form, "id": id})


def delete_album(request, id):
    album = Album.objects.get(id=id)

    if request.method == "POST":
        album.delete()
        return redirect("home")

    form = DeleteAlbumForm(instance=album)

    return render(request, "delete-album.html", {"form": form, "id": id})

