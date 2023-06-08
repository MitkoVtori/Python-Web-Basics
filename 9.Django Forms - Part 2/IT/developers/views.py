from django.shortcuts import render, redirect, get_object_or_404

from IT.developers.forms import DeveloperForm
from IT.developers.models import Developer


def index(request):
    form = DeveloperForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')

    return render(request, 'index.html', {"form": form})


def update_name(request, developer_id):
    name = get_object_or_404(Developer, developer_id=developer_id)
    form = DeveloperForm(request.POST or None, instance=name)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'update.html', {"form": form, "developer_id": developer_id})


def success(request):
    return render(request, 'success.html')


def developers(request):
    return render(request, "developers.html", {"developers": Developer.objects.all().order_by("developer_id")})
