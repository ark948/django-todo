from todo.forms import NewTaskForm
from django.test import SimpleTestCase

class TestNewTaskForm(SimpleTestCase):
    def setUp(self) -> None:
        self.form = NewTaskForm()
        return super().setUp()
    
    def test_field_labels(self):
        self.assertEqual(self.form.fields['title'].label, "عنوان")

    def test_field_lengths(self):
        self.assertEqual(self.form.fields['title'].max_length, 50)