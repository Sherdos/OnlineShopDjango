from django import forms
from product.models import choices_review
from product.models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ReviewForm(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choices_review, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
    # TODO: Define form fields here

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
