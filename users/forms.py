from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    """Form for register."""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """Form for profile info."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'preview')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()