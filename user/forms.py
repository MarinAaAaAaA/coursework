from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Имя пользователя')
    password = forms.CharField(required=True, widget=forms.PasswordInput, label='Пароль')

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, label='Имя пользователя')
    email = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(required=True, widget=forms.PasswordInput, label='Пароль')