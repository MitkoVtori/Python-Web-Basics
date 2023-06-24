from django.shortcuts import render, redirect

from FruitipediaApp.Fruit.forms import EditFruitForm, DeleteFruitForm
from FruitipediaApp.Fruit.models import Fruit


def fruit_details(request, fruitid):
    fruit = Fruit.objects.get(id=fruitid)
    return render(request, "details-fruit.html", {"fruit": fruit})


def edit_fruit(request, fruitid):
    fruit = Fruit.objects.get(id=fruitid)
    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(request, "edit-fruit.html", {"form": form, "fruitid": fruitid})


def delete_fruit(request, fruitid):
    fruit = Fruit.objects.get(id=fruitid)

    if request.method == 'POST':
        fruit.delete()
        return redirect("dashboard")

    form = DeleteFruitForm(instance=fruit)
    return render(request, "delete-fruit.html", {"form": form, "fruitid": fruitid})