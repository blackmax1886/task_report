from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

from .models import Task


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
    return HttpResponse("This page show No.%s task detail.", pk)
