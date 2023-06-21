from django import forms
from MyMusicApp.MyMusicApp.Profile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

