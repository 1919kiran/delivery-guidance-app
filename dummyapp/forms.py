from django import forms
from .models import AuthModel


class RobinForm(forms.Form):
    name = forms.CharField()
    contact = forms.CharField()
    designation = forms.ChoiceField(choices=(('SPOC', 'SPOC'), ('Robin', 'Robin'), ('Guest', 'Guest')))
    #designation = forms.CharField()
    email = forms.EmailField()
    location = forms.CharField()
    pwd1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    transport = forms.ChoiceField(choices=(('Car', 'Car'), ('Bike', 'Bike'), ('Truck', 'Truck')))
    #transport = forms.CharField()

class DonorForm(forms.Form):
    name = forms.CharField()
    contact = forms.CharField() 
    email = forms.EmailField()
    location = forms.CharField()
    pwd1 = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginRobin(forms.Form):
    email = forms.CharField()
    pwd1 = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginDonor(forms.Form):
    email = forms.CharField()
    pwd1 = forms.CharField(max_length=32, widget=forms.PasswordInput)

class CreateFoodForm(forms.Form):
    type = forms.ChoiceField(choices=(('packaged', 'packaged'),('cooked', 'cooked')))
    name = forms.CharField()
    quantity = forms.CharField()
    location = forms.CharField()

class AuthForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        fields = [
            "image",
        ]
