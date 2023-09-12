from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "confirm_password"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "confirm_password"]

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "first name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "last name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "username"}))
    # password = forms.CharField(widget=forms.PasswordInput())
    # confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        clean_data = super(SignupForm, self).clean()

        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")