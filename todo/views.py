from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from todo.models import Task, TaskStatus
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.forms import NewTaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

class TodoHomePage(LoginRequiredMixin, ListView): # unused
    template_name = "todo/index.html"
    context_object_name = "todays_tasks"
    login_url = "account_login"

    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.filter(owner__pk=self.request.user.pk)

@login_required    
def index(request):
    context = {}
    todays_tasks = Task.objects.filter(owner__pk=request.user.pk).order_by("created")
    context['todays_tasks'] = todays_tasks
    context['new_task_form'] = NewTaskForm()
    return render(request, "todo/index.html", context=context)

@login_required
def new_task_process(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            try:
                new_task = Task()
                new_status = TaskStatus.objects.get(name="In_progress")
                new_task.title = form.cleaned_data['title']
                new_task.details = form.cleaned_data['details']
                new_task.owner = request.user
                new_task.status = new_status
                new_task.save()
                messages.success(request, "مخاطب افزوده شد")
            except Exception as error:
                print(error)
                messages.error(request, "خطا")
        else:
            print(form.errors)
            messages.error(request, "خطا در فرم")
    return redirect("todo:index")