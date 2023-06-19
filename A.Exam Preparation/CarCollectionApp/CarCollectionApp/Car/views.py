from django.shortcuts import render, redirect, get_object_or_404
from CarCollectionApp.CarCollectionApp.Car.models import Car
from CarCollectionApp.CarCollectionApp.Car.forms import CarForm, DeleteCarForm
from CarCollectionApp.CarCollectionApp.Profile.models import Profile


def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("catalogue")

    return render(request, 'car-create.html', {"form": form, "profile": Profile.objects.first()})


def car_details(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, "car-details.html", {"car": car, "profile": Profile.objects.first()})


def car_edit(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect("catalogue")

    return render(request, "car-edit.html", {"form": form, "profile": Profile.objects.first(), "car_id": car_id})


def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect("catalogue")

    form = DeleteCarForm(instance=car)

    return render(request, "car-delete.html", {"form": form, "profile": Profile.objects.first(), "car_id": car_id})