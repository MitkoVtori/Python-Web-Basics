from django import forms
from CarCollectionApp.CarCollectionApp.Car.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

