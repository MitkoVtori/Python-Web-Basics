from django import forms
from FruitipediaApp.Profile.models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')

    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    class Meta:
        model = Profile
        exclude = ['image_url', 'age']


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='First Name')

    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='Last Name')

    image_url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Image URL'}), label='Image URL',
                               required=False)

    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}), label='Age', required=False)

    class Meta:
        model = Profile
        exclude = ['email', 'password']

