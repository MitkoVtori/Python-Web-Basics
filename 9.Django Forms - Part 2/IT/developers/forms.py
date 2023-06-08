from django import forms
from .models import Developer


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

    def clean(self):
        super(DeveloperForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        if len(first_name) == 3:
            self._errors['first_name'] = self.error_class(['Test error on name with three letters!'])
        return self.cleaned_data
