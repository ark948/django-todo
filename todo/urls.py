from django.urls import path
from todo.views import index, new_task_process

app_name = "todo"
urlpatterns = [
    path("", index, name="index"),
    path("new-task/", new_task_process, name="new"),
]