from django import forms
from FruitipediaApp.Fruit.models import Fruit


class FruitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fruit Name'}), label='')

    image_url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}), label='')

    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Fruit Description'}), label='')

    nutrition = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nutrition Info'}), label='', required=False)

    class Meta:
        model = Fruit
        fields = '__all__'


class EditFruitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Fruit Name'}), label='Name')

    image_url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}), label='Image URL')

    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Fruit Description'}), label='Description')

    nutrition = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nutrition Info'}), label='Nutrition',
                                required=False)

    class Meta:
        model = Fruit
        fields = '__all__'


class DeleteFruitForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput, label='Name',
                           disabled=True)

    image_url = forms.URLField(widget=forms.URLInput, label='Image URL',
                               disabled=True)

    description = forms.CharField(widget=forms.Textarea, label='Description',
                                  disabled=True)

    class Meta:
        model = Fruit
        exclude = ['nutrition']

