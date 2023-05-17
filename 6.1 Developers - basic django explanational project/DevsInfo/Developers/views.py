from django.shortcuts import render, redirect

from DevsInfo.Developers.models import Developer


def home_page(request):
    developers = Developer.objects.all()
    context = {
        'developers': developers,
    }
    return render(request, 'html/index.html', context)


def some(request):
    return redirect('home')