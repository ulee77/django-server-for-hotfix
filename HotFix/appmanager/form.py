__author__ = 'uwen'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    # first_name = forms.CharField()
    # last_nmae = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1= forms.CharField(label='Confirm', widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2