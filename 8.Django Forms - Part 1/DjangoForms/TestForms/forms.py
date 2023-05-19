from django import forms
from .models import Name


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = '__all__'


class WebsiteForm(forms.Form):
    your_website = forms.CharField(label="Website", initial='https://', max_length=250, required=False)


class GenderForm(forms.Form):
    CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
    )

    gender = forms.ChoiceField(label="Gender", choices=CHOICES)

