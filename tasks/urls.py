from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    # ex: /tasks/
    path('', views.index, name='index'),
    # ex: /tasks/4/
    path('<int:pk>/', views.detail, name='detail')
]