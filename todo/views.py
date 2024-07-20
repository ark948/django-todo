from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from todo.models import Task

# Create your views here.

class TodoHomePage(ListView):
    template_name = "todo/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.filter(owner__pk=self.request.user.pk)