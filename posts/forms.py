from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "inputs", "placeholder": "Enter username.."}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "inputs", "placeholder": "Enter password.."}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "inputs", "placeholder": "Enter password again.."}), label="Confirm Password")

    class Meta:
        # we can't give labels etc in class Meta to these feilds username, password1, password2
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"email": "Email"}
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "inputs", "placeholder": "Enter first name.."}),
            "last_name": widgets.TextInput(attrs={"class": "inputs", "placeholder": "Enter last name.. (optional)"}),
            "email": widgets.EmailInput(attrs={"class": "inputs", "placeholder": "Enter email.."}),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Tyoe username...", "class": "inputs"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password", "class": "inputs"}))
