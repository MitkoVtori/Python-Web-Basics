from django import forms
from CarCollectionApp.CarCollectionApp.Profile.models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"

