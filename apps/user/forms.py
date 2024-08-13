from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    email = forms.EmailField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email', 'autocomplete': 'off', 'required': 'true'}))
    full_name = forms.CharField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(max_length=255, label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    email = forms.EmailField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email', 'autocomplete': 'off', 'required': 'true'}))
    full_name = forms.CharField(max_length=255, label=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    password1 = forms.CharField(max_length=255, label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(max_length=255, label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')