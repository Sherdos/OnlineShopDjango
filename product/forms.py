from django import forms
from product.models import choices_review
from product.models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class ReviewForm(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choices_review, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
    # TODO: Define form fields here

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}),label='Имя пользователя')
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
