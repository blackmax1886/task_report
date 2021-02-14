from django.views import generic
from django.urls import reverse_lazy

from .models import Task, Subtask
from .forms import TaskForm


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
