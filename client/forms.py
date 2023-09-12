from django import forms
from .models import ClientProfile
from django.contrib.auth.models import User



class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ["profile_pic", "address", "phone_number"]
        read_only_fields = ["phone_number"]

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-line"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-line", "readonly": "True"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-line"}))




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-line"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-line"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-line"}))



class OPTForm(forms.Form):
    otp1 = forms.CharField(min_length=6, max_length=6, widget=forms.TextInput(attrs={"class": "form-control form-control-line"}))
    otp2 = forms.CharField(min_length=6, max_length=6, widget=forms.TextInput(attrs={"class": "form-control form-control-line"}))



