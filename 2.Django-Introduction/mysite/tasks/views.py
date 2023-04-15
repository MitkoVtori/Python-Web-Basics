from django.http import HttpResponse
from django.shortcuts import render
from mysite.tasks.models import Task, Diet


def index(request):
    return render(request, "index.html")


def tasks(request):
    tasks_list = Task.objects.all()
    output = '; '.join(f"{task.Name}: {task.Description}" for task in tasks_list)

    if not output:
        output = "--- There are no tasks ---"

    output += '<br><br><br><button style="background-color: black; width: 70px; height: 45px; font-size: 25px"><a style="color: yellow" href="http://127.0.0.1:8000/tasks/diets/">Diets</a></button>'

    return HttpResponse(output)


def diets(request):
    diets_list = Diet.objects.all()
    output = '; '.join(f"{diet.Name}: {diet.Description}" for diet in diets_list)

    if not output:
        output = "-!- There are no diets -!-"

    output += '<br><br><br><button style="background-color: black; width: 75px; height: 50px; font-size: 18px"><a style="color: yellow" href="http://127.0.0.1:8000/tasks/">Tasks</a></button>'

    return HttpResponse(output)

