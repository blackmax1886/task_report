from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('singup/', views.Signup.as_view(), name='signup')
]
