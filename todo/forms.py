from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="عنوان")
    details = forms.TextInput(label="جزئیات")
