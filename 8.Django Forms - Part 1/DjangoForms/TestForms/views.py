from django.shortcuts import render, redirect

from DjangoForms.TestForms.forms import NameForm, WebsiteForm, GenderForm


def index(request):
    if request.method == "GET":
        name_form = NameForm()
        website_form = WebsiteForm()
        gender_form = GenderForm()

    if request.method == "POST":
        name_form = NameForm(request.POST)
        website_form = WebsiteForm(request.POST or None)
        gender_form = GenderForm(request.POST)

        if name_form.is_valid() and website_form.is_valid() and gender_form.is_valid():
            name_form.save()
            return redirect('success')

    context = {
        "form": name_form,
        'site': website_form,
        'gender': gender_form,
    }

    return render(request, 'index.html', context)


def successful_form_fill(request):
    return render(request, 'success.html')
