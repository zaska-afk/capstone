from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    display_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class LoginForm(forms.Form):
    username = forms.CharField(label="Enter a Valid Username")
    password = forms.CharField(label="Enter a Valid Password", widget=forms.PasswordInput())
    