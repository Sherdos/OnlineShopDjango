from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Пароль', help_text="Пароль не должен быть слишком похож на другую вашу личную информацию.")
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Подтверждение пароля', help_text= 'Для подтверждения введите, пожалуйста, пароль ещё раз.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')