from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from apps.user.forms import LoginForm, RegisterForm
from django.views.generic import CreateView

# Create your views here.
class LoginView(LoginView):
    template_name = 'login/login.html'
    form_class = LoginForm

class SignUpView(CreateView):
    template_name = 'login/register.html'
    form_class = RegisterForm
    success_url = '/'
