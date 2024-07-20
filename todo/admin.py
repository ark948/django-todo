from django.contrib import admin
from todo.models import TaskStatus, Task

# Register your models here.

admin.site.register(TaskStatus)
admin.site.register(Task)