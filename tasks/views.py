from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView

from .models import Task, Subtask
from .forms import TaskForm


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'closest_task_list'

    def get_queryset(self):
        """Return the 5 closest uncompleted tasks to deadline."""
        return Task.objects.filter(status=False).order_by('-deadline')[:5:-1]


class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/form.html"
    success_url = "/"
