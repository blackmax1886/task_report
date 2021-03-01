from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import reverse_lazy

from django.views import generic
from .forms import LoginForm, SignupForm


class Top(generic.TemplateView):
    template_name = 'users/top.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'users/login.html'


class Signup(generic.CreateView):
    form_class = SignupForm
    template_name = "users/signup.html"
    success_url = reverse_lazy('users:top')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
