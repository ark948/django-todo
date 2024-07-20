from django.test import TestCase
from todo.views import TodoHomePage
from todo.models import Task, TaskStatus
from django.urls import reverse

class TestTodoHomePage(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def test_todohomepage_correct_template(self):
        response = self.client.get(reverse("todo:index"))
        self.assertTemplateUsed(response, "todo/index.html")