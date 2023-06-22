from django import forms
from GamesPlayApp.Profile.models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ["email", "age", "password"]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

