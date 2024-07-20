from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.

class TodoHomePage(TemplateView):
    template_name = "todo/index.html"