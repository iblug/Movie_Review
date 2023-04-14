from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        min_length=6,
    )

    email = forms.CharField(
        widget=forms.EmailInput(
        )
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )