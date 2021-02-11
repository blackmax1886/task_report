from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from .models import Task, Subtask


# class IndexView(TemplateView):
#     template_name = "index.html"


def index(request):
    latest_task_list = Task.objects.order_by('-deadline')[:5]
    template = loader.get_template('tasks/index.html')
    context = {
        'latest_task_list': latest_task_list,
    }
    return render(request, 'tasks/index.html', context)


def detail(request, pk):
    task = Task.objects.get(id=pk)
    subtasks = Subtask.objects.filter(task=task)
    context = {
        'task': task,
        'subtasks': subtasks
    }
    return render(request, 'tasks/detail.html', context)
