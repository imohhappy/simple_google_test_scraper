from django import forms


class Login(forms.Form):
    username = forms.CharField(label='Enter Username ')
    password = forms.CharField(label='Enter Password ')


class Create(forms.Form):
    name = forms.CharField()
    phone_number = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(label='Enter Password ')
    verify_password = forms.CharField(label='Please re-enter Password')
