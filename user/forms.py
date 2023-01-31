from django import forms

class BaseForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=32)

class RegisterForm(BaseForm):
    email = forms.CharField(max_length=32)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=32)