from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # Help Messages
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    firstName = forms.CharField(label='Name')
    lastName = forms.CharField(label='LastName')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'firstName', 'lastName']
        help_texts = {k: "" for k in fields}
