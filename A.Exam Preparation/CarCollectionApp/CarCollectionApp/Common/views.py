from django.shortcuts import render
from CarCollectionApp.CarCollectionApp.Profile.models import Profile
from CarCollectionApp.CarCollectionApp.Car.models import Car


def index(request):
    profile = Profile.objects.first()
    context = {"profile": profile}

    return render(request, 'index.html', context)


def catalogue(request):
    context = {
        "profile": Profile.objects.first(),
        "cars": Car.objects.all()
    }

    return render(request, "catalogue.html", context)

