from django.shortcuts import render, redirect

from FruitipediaApp.Fruit.models import Fruit
from FruitipediaApp.Profile.forms import ProfileForm, EditProfileForm
from FruitipediaApp.Profile.models import Profile


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'create-profile.html', {"form": form})


def profile_details(request):
    return render(request, "details-profile.html", {"fruits": Fruit.objects.all()})


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("profile")

    return render(request, "edit-profile.html", {"form": form})


def delete_profile(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    if request.method == "POST":
        profile.delete()
        fruits.delete()
        return redirect("home")

    return render(request, "delete-profile.html")