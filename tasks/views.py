from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# class IndexView(TemplateView):
#     template_name = "index.html"


def index(request):
    return HttpResponse("This page is going to show your tasks")


def detail(request, pk):
    return HttpResponse("This page show No.%s task detail.", pk)