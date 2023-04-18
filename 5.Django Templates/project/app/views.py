from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'first_name': 'Peter',
        'last_name': 'Ivanov',
        'three_names': ['Peter', 'Jordan', 'Ivanov'],
        'date': datetime.now(),
        'Age': 27,
        'Job': 'Programmer',
        'words': 'I am a software engineer!',
        'empty': '',
        'not_empty': '1',
        'colleagues': ["Steve", "Josh", "Gorge", "Peter 2.", "Sam"],
        'url': 'https://github.com',
        'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def go_home(request):
    return render(request, 'go_home.html')