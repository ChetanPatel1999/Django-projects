from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_class = (
            "w-full px-4 py-2 border border-gray-300 rounded-lg "
            "focus:outline-none focus:ring-2 focus:ring-blue-500 "
            "focus:border-blue-500 transition"
        )

        self.fields['username'].widget.attrs.update({
            'class': input_class,
            'placeholder': 'Enter username'
        })

        self.fields['email'].widget.attrs.update({
            'class': input_class,
            'placeholder': 'Enter email address'
        })

        self.fields['password1'].widget.attrs.update({
            'class': input_class,
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': input_class,
            'placeholder': 'Confirm password'
        })