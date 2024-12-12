from django import forms
from todo.models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"
