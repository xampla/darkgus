from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hcaptcha_field import hCaptchaField


class DomainCheckForm(forms.Form):
    domain = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'class': 'search-input', 'placeholder': 'Enter a domain...'}))
    hcaptcha = hCaptchaField(label='', theme='dark', size='compact')

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
