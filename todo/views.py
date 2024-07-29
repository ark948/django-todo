from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView
from todo.models import Task, TaskStatus
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.forms import NewTaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.serializers import serialize

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

@login_required
def delete_task(request):
    if request.method == "POST":
        task_to_delete = Task.objects.get(pk=int(request.POST.get("id_to_delete")))
        try:
            if task_to_delete.owner.id == request.user.id:
                task_to_delete.delete()
                messages.info(request, "مخاطب حذف شد.")
        except Exception as error:
            print(error)
            messages.error(request, "خطایی رخ داده است.")
    return redirect("todo:index")   

def get_data(request):
    # ajax
    data = {'message': "Hello from ajax"}
    return JsonResponse(data)

def get_tasks(request):
    context = {}
    first_task = Task.objects.filter(owner__pk=request.user.pk).first()
    data = serialize("json", [first_task], fields=('title'))
    # todays_tasks = Task.objects.filter(owner__pk=request.user.pk).order_by("created")
    # return JsonResponse({'todos': list(todays_tasks.values())})
    return JsonResponse(data, safe=False)

def test_request_type(request):
    if request.is_ajax():
        data = {"message": "YES AJAX"}
    else:
        data = {"message": "NOT AJAX"}
    return JsonResponse(data=data)
    