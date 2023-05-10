from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def show_details_page(request):
    return render(request, template_name='pets/pet-details-page.html')


def edit_page(request):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request):
    return render(request, template_name='pets/pet-delete-page.html')

