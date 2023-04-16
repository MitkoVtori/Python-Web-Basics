from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("<h1>Valid urls:</h1><h6>1. department/&lt;int:department_id&gt;/</h6> \
                        <h6>2. department/&lt;str:department_name&gt;/</h6><h6>3. worker/&lt;int:worker_id&gt;/</h6>")


def show_department_by_id(request, department_id):
    if department_id == 1:
        department_name = "Developers"
    elif department_id == 2:
        department_name = "Trainers"
    elif department_id == 3:
        department_name = "QAs"
    else:
        return HttpResponseNotFound("Department was not found!")

    html = "<html><body><h1>" \
           "Department Name: %s, Department ID: %s" \
           "</h1></body></html>" \
           % (department_name, department_id)

    return HttpResponse(html)


def show_department_by_name(request, department_name):
    if department_name.lower() in ["dev", "developers", "devs"]:
        return redirect('http://127.0.0.1:8000/department/1/')
    elif department_name.lower() in ["trainer", "trainers"]:
        return redirect('http://127.0.0.1:8000/department/2/')
    elif department_name.lower() in ['qa', 'qas', 'quality assurance', 'quality assurances']:
        return redirect('http://127.0.0.1:8000/department/3/')
    else:
        return HttpResponseNotFound("Department was not found!")


def show_worker_by_id(request, worker_id):
    if worker_id < 1:
        return render(request, "404.html")

    workers = {1: "Steve: Developer", 2: "Markus: Developer", 3: "George: Quality Assurance", 4: "Hannah: Trainer"}

    if worker_id not in workers.keys():
        return HttpResponse(status=501)

    html = "<html><body><h1>" \
           "%s, Department ID: %s" \
           "</h1></body></html>" \
           % (workers[worker_id], worker_id)

    return HttpResponse(html)

