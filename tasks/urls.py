from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # ex: /tasks/
    path('', views.index, name='index'),
    # ex: /tasks/4/
    path('<int:task_id>/', views.detail, name='detail')
]