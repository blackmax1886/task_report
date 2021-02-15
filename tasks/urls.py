from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # ex: /tasks/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /tasks/4/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /tasks/new/
    path('new/', views.TaskCreateView.as_view(), name='create'),
    # ex: /tasks/4/subtask/new
    path('<int:pk>/subtask/new', views.SubtaskCreateView.as_view(template_name='tasks/create.html'), name='create_sub')
]
