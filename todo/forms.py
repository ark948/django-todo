from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(label="عنوان", max_length=50, required=True)
    details = forms.CharField(widget=forms.Textarea)