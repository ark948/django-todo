from django.db import models
from django.conf import settings

# Create your models here.


class TaskStatus(models.Model):
    name = models.CharField("name", null=False, blank=False, max_length=30)

    def __str__(self):
        return f"Status of task {self.name}"
    
    class Meta:
        verbose_name = "TaskStatus"
        verbose_name_plural = "TaskStatuses"
    

class Task(models.Model):
    title = models.CharField("Title", null=False, blank=False, max_length=50)
    details = models.TextField("Details", null=True, blank=True)
    created = models.DateTimeField("Created on", auto_now_add=True)
    status = models.ForeignKey(TaskStatus, unique=False, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
