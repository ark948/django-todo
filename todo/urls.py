from django.urls import path
from todo.views import index, new_task_process, get_data, get_tasks, delete_task

app_name = "todo"
urlpatterns = [
    path("", index, name="index"),
    path("new-task/", new_task_process, name="new"),
    path("delete-single-task", delete_task, name='delete-task'),
    path('ajax/get_data', get_data, name='get_data'),
    path('ajax/get_tasks', get_tasks, name='get_tasks'),
]