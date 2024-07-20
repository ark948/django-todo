from django.test import TestCase
from todo.models import Task, TaskStatus
from django.contrib.auth import get_user_model

class TaskStatusModelTest(TestCase):
    @classmethod
    def setUpTestData(self) -> None:
        self.task_status = TaskStatus.objects.create(name="Completed")

    def test_task_status_labels(self):
        name_label = self.task_status._meta.get_field('name').verbose_name
        self.assertEqual(name_label, "name")

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.task_status = TaskStatus.objects.create(name="Completed")
        cls.user = get_user_model().objects.create(username="testuser", password="hello123*")
        cls.task = Task.objects.create(title="task 1", status=cls.task_status, owner=cls.user)
        return super().setUpTestData()
    
    def test_setUpTestData_was_ok(self):
        # test if setUpTestData passes (if this test is reached)
        self.assertTrue(True)

    def test_user_owns_task(self):
        self.owner = self.task.owner
        self.assertTrue(isinstance(self.owner, get_user_model()))

    def test_task_has_status(self):
        self.assertEqual(self.task.status, self.task_status)

    def test_task_title_is_correct(self):
        self.assertEqual(self.task.title, "task 1")