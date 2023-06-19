from django.shortcuts import render, redirect

from CarCollectionApp.CarCollectionApp.Car.models import Car
from CarCollectionApp.CarCollectionApp.Profile.forms import ProfileForm, EditProfileForm
from CarCollectionApp.CarCollectionApp.Profile.models import Profile


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("catalogue") # catalogue

    return render(request, 'profile-create.html', {"form": form, "profile": Profile.objects.first()})


def profile_details(request):
    total_cars_price = 0
    for car in Car.objects.all():
        total_cars_price += car.price

    return render(request, "profile-details.html", {"profile": Profile.objects.first(), "price": f"{total_cars_price:.2f}"})


def profile_edit(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("catalogue")

    return render(request, "profile-edit.html", {"form": form, "profile": profile})


def delete_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()

        return redirect('home')

    return render(request, 'profile-delete.html', {"profile": Profile.objects.first()})