from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Task, Subtask
from .forms import TaskForm, SubtaskForm


class IndexView(generic.ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'closest_task_list'
    paginate_by = 5

    def get_queryset(self):
        """Return the uncompleted tasks ordered by deadline."""
        return Task.objects.filter(status=False).order_by('-deadline')[::-1]


class DetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/detail.html'


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy('tasks:index')


class SubtaskCreateView(generic.CreateView):
    model = Subtask
    form_class = SubtaskForm
    template_name = "tasks/create.html"

    def get_success_url(self):  # 詳細画面にリダイレクトする。
        return reverse_lazy('tasks:detail', kwargs={'pk': self.kwargs['pk']})