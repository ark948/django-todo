from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TodoHomePage(LoginRequiredMixin, ListView):
    template_name = "todo/index.html"
    context_object_name = "todays_tasks"
    login_url = "account_login"

    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.filter(owner__pk=self.request.user.pk)