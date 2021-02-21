from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Subtask
from .forms import TaskForm, SubtaskForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'closest_task_list'
    paginate_by = 5

    def get_queryset(self):
        """Return the uncompleted tasks ordered by deadline."""
        return Task.objects.filter(create_user=self.request.user, status=False).order_by('-deadline')[::-1]


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


def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.status = True
        task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


def subcomplete(request, task_id, subtask_id):
    task = get_object_or_404(Task, pk=task_id)
    subtask = task.subtask_set.get(id=subtask_id)
    if request.method == 'POST':
        if 'complete' in request.POST:
            subtask.status = True
            subtask.save()
        elif 'working' in request.POST:
            subtask.status = False
            subtask.save()
    return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))
