from django.shortcuts import render
from . import models


def index(requests):
    contacts = models.Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(requests, 'index.html', context)
