from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)