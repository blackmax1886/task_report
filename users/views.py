from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)

from django.views import generic
from .forms import LoginForm


class Top(generic.TemplateView):
    template_name = 'users/top.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'users/login.html'